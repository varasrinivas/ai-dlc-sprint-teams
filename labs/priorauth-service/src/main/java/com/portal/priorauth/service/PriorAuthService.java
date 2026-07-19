package com.portal.priorauth.service;

import com.portal.priorauth.domain.AuthStatus;
import com.portal.priorauth.domain.PriorAuthRequest;
import com.portal.priorauth.repository.PriorAuthRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.NoSuchElementException;

/**
 * Application service for prior auth requests.
 *
 * This is the "use case" layer: it coordinates the rules engine and the repository.
 * Controllers call into here; they never touch the repository directly.
 */
@Service
public class PriorAuthService {

    private final PriorAuthRepository repository;
    private final AutoApprovalService autoApproval;

    public PriorAuthService(PriorAuthRepository repository, AutoApprovalService autoApproval) {
        this.repository = repository;
        this.autoApproval = autoApproval;
    }

    /**
     * Submit a new request. The rules engine scores it immediately: routine requests are
     * auto-approved, everything else is routed to a human reviewer.
     */
    @Transactional
    public PriorAuthRequest submit(String memberId, String providerNpi, String serviceCode,
                                   String diagnosisCode, int requestedUnits) {
        PriorAuthRequest request = new PriorAuthRequest(
                memberId, providerNpi, serviceCode, diagnosisCode, requestedUnits);

        double score = autoApproval.score(request);
        String reason = autoApproval.explain(request);
        AuthStatus outcome = autoApproval.canAutoApprove(request)
                ? AuthStatus.APPROVED
                : AuthStatus.PENDING_REVIEW;

        request.applyDecision(outcome, score, reason);
        return repository.save(request);
    }

    @Transactional(readOnly = true)
    public PriorAuthRequest getById(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new NoSuchElementException(
                        "No prior auth request found with id " + id));
    }

    @Transactional(readOnly = true)
    public List<PriorAuthRequest> list(AuthStatus status) {
        return status == null ? repository.findAll() : repository.findByStatus(status);
    }

    /**
     * A reviewer's final decision on a request that was pending review.
     * Only PENDING_REVIEW requests can be decided this way.
     */
    @Transactional
    public PriorAuthRequest decide(Long id, AuthStatus decision, String reason) {
        if (decision != AuthStatus.APPROVED && decision != AuthStatus.DENIED) {
            throw new IllegalArgumentException("A reviewer decision must be APPROVED or DENIED.");
        }
        PriorAuthRequest request = getById(id);
        if (request.getStatus() != AuthStatus.PENDING_REVIEW) {
            throw new IllegalStateException(
                    "Only requests in PENDING_REVIEW can be decided. Current status: "
                            + request.getStatus());
        }
        request.applyDecision(decision, request.getApprovalScore(), reason);
        return repository.save(request);
    }
}
