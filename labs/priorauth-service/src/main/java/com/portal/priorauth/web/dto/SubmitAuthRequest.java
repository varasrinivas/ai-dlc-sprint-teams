package com.portal.priorauth.web.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

/**
 * Incoming payload for submitting a prior auth request.
 *
 * Validation annotations run automatically before the controller method executes
 * (because the controller marks this parameter with @Valid).
 */
public record SubmitAuthRequest(

        @NotBlank(message = "memberId is required")
        String memberId,

        @NotBlank(message = "providerNpi is required")
        @Pattern(regexp = "\\d{10}", message = "providerNpi must be exactly 10 digits")
        String providerNpi,

        @NotBlank(message = "serviceCode is required")
        String serviceCode,

        @NotBlank(message = "diagnosisCode is required")
        String diagnosisCode,

        @Min(value = 1, message = "requestedUnits must be at least 1")
        int requestedUnits
) {
}
