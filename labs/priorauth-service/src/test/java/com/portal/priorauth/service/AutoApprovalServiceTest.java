package com.portal.priorauth.service;

import com.portal.priorauth.domain.PriorAuthRequest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * A starter test for the rules engine.
 *
 * There is deliberately only ONE example here. In the course you'll use an AI assistant
 * to grow this into a full suite (edge cases, the exact threshold boundary, and more).
 */
class AutoApprovalServiceTest {

    private final AutoApprovalService service = new AutoApprovalService();

    @Test
    @DisplayName("A routine office visit is auto-approved")
    void routineVisitIsAutoApproved() {
        PriorAuthRequest routine = new PriorAuthRequest(
                "MBR-1001", "1234567890", "99213", "M54.5", 1);

        assertThat(service.score(routine)).isGreaterThanOrEqualTo(AutoApprovalService.AUTO_APPROVE_THRESHOLD);
        assertThat(service.canAutoApprove(routine)).isTrue();
    }
}
