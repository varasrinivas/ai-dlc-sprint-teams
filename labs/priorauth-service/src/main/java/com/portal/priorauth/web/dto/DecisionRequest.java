package com.portal.priorauth.web.dto;

import com.portal.priorauth.domain.AuthStatus;
import jakarta.validation.constraints.NotNull;

/**
 * A reviewer's decision on a pending request.
 * "decision" must be APPROVED or DENIED (enforced in the service layer).
 */
public record DecisionRequest(

        @NotNull(message = "decision is required (APPROVED or DENIED)")
        AuthStatus decision,

        String reason
) {
}
