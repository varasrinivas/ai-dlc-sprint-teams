package com.portal.priorauth.service;

import com.portal.priorauth.domain.PriorAuthRequest;
import org.springframework.stereotype.Service;

import java.util.Set;

/**
 * Decides whether a prior auth request can be auto-approved.
 *
 * The engine produces a confidence score between 0.0 and 1.0. If the score is at or above
 * AUTO_APPROVE_THRESHOLD, the request is auto-approved. Otherwise it is routed to a human
 * reviewer (PENDING_REVIEW).
 *
 * The scoring is intentionally simple and explainable so it is easy to reason about, test,
 * and later refactor. Several course labs live inside this class.
 */
@Service
public class AutoApprovalService {

    /** Requests scoring at or above this value are auto-approved. */
    public static final double AUTO_APPROVE_THRESHOLD = 0.85;

    /** Every request starts from this baseline confidence. */
    private static final double BASE_SCORE = 0.90;

    /** Service codes that always warrant a closer look (e.g. high-cost imaging). */
    private static final Set<String> REVIEW_REQUIRED_SERVICES = Set.of(
            "70551", // MRI brain without contrast
            "72148", // MRI lumbar spine without contrast
            "J9299"  // high-cost injectable
    );

    /** Requests above this many units draw extra scrutiny. */
    private static final int HIGH_UNIT_THRESHOLD = 10;

    /**
     * Score a request from 0.0 to 1.0. Higher means more confidently routine.
     * Penalties stack; the result is clamped to [0.0, 1.0].
     */
    public double score(PriorAuthRequest request) {
        double score = BASE_SCORE;

        if (REVIEW_REQUIRED_SERVICES.contains(request.getServiceCode())) {
            score -= 0.20;
        }
        if (request.getRequestedUnits() > HIGH_UNIT_THRESHOLD) {
            score -= 0.15;
        }
        if (request.getDiagnosisCode() == null || request.getDiagnosisCode().isBlank()) {
            score -= 0.10;
        }

        return clamp(score);
    }

    /** True when the request's score clears the auto-approval bar. */
    public boolean canAutoApprove(PriorAuthRequest request) {
        return score(request) >= AUTO_APPROVE_THRESHOLD;
    }

    /** A short, human-readable explanation for the score - shown to reviewers and providers. */
    public String explain(PriorAuthRequest request) {
        double score = score(request);
        if (score >= AUTO_APPROVE_THRESHOLD) {
            return String.format("Auto-approved: routine request scored %.2f (threshold %.2f).",
                    score, AUTO_APPROVE_THRESHOLD);
        }
        return String.format("Routed for review: request scored %.2f, below the %.2f threshold.",
                score, AUTO_APPROVE_THRESHOLD);
    }

    private double clamp(double value) {
        return Math.max(0.0, Math.min(1.0, value));
    }
}
