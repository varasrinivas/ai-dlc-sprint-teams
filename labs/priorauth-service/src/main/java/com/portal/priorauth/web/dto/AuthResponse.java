package com.portal.priorauth.web.dto;

import com.portal.priorauth.domain.AuthStatus;
import com.portal.priorauth.domain.PriorAuthRequest;

import java.time.Instant;

/**
 * What the API returns to callers. Keeping a separate response record (rather than exposing
 * the JPA entity directly) means we control exactly which fields leave the service.
 */
public record AuthResponse(
        Long id,
        String memberId,
        String providerNpi,
        String serviceCode,
        String diagnosisCode,
        int requestedUnits,
        AuthStatus status,
        Double approvalScore,
        String decisionReason,
        Instant submittedAt,
        Instant decidedAt
) {
    /** Map a domain entity into its API representation. */
    public static AuthResponse from(PriorAuthRequest r) {
        return new AuthResponse(
                r.getId(),
                r.getMemberId(),
                r.getProviderNpi(),
                r.getServiceCode(),
                r.getDiagnosisCode(),
                r.getRequestedUnits(),
                r.getStatus(),
                r.getApprovalScore(),
                r.getDecisionReason(),
                r.getSubmittedAt(),
                r.getDecidedAt()
        );
    }
}
