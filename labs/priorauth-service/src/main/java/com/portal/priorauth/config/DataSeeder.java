package com.portal.priorauth.config;

import com.portal.priorauth.service.PriorAuthService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Seeds a few example requests when the app starts, so there is data to explore
 * immediately at GET /api/v1/prior-auth.
 *
 * The three rows are chosen to show every path through the rules engine:
 *   - a routine visit that auto-approves
 *   - a high-cost MRI that is routed for review
 *   - a large-unit request that is routed for review
 */
@Configuration
public class DataSeeder {

    @Bean
    CommandLineRunner seed(PriorAuthService service) {
        return args -> {
            // Routine office visit -> should auto-approve (score 0.90).
            service.submit("MBR-1001", "1234567890", "99213", "M54.5", 1);

            // MRI brain -> review-required service, score drops below 0.85.
            service.submit("MBR-1002", "1234567890", "70551", "R51.9", 1);

            // Large-unit physical therapy -> high units push it below the threshold.
            service.submit("MBR-1003", "9876543210", "97110", "M25.561", 24);
        };
    }
}
