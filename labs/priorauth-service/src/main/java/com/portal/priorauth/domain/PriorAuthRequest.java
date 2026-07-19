package com.portal.priorauth.domain;

import jakarta.persistence.*;

import java.time.Instant;

/**
 * A single prior authorization request submitted by a provider on behalf of a member.
 *
 * This is a JPA entity: each instance maps to one row in the PRIOR_AUTH_REQUEST table.
 * Keep it focused on data + simple lifecycle helpers; business rules live in the service layer.
 */
@Entity
@Table(name = "prior_auth_request")
public class PriorAuthRequest {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    /** The member (patient) this request is for. */
    @Column(nullable = false)
    private String memberId;

    /** The provider's 10-digit National Provider Identifier. */
    @Column(nullable = false)
    private String providerNpi;

    /** The requested service / procedure code (CPT-style, e.g. "99213" or "70551"). */
    @Column(nullable = false)
    private String serviceCode;

    /** The supporting diagnosis code (ICD-style, e.g. "M54.5"). */
    @Column(nullable = false)
    private String diagnosisCode;

    /** How many units of the service are being requested. */
    @Column(nullable = false)
    private int requestedUnits;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private AuthStatus status;

    /** Confidence score (0.0 - 1.0) produced by the rules engine. Null until scored. */
    private Double approvalScore;

    /** Human-readable explanation of the current status. */
    @Column(length = 500)
    private String decisionReason;

    @Column(nullable = false)
    private Instant submittedAt;

    /** When a final decision (approve/deny) was reached. Null while still open. */
    private Instant decidedAt;

    protected PriorAuthRequest() {
        // Required by JPA.
    }

    public PriorAuthRequest(String memberId, String providerNpi, String serviceCode,
                            String diagnosisCode, int requestedUnits) {
        this.memberId = memberId;
        this.providerNpi = providerNpi;
        this.serviceCode = serviceCode;
        this.diagnosisCode = diagnosisCode;
        this.requestedUnits = requestedUnits;
        this.status = AuthStatus.SUBMITTED;
        this.submittedAt = Instant.now();
    }

    /** Record the outcome of scoring or a reviewer decision. */
    public void applyDecision(AuthStatus newStatus, Double score, String reason) {
        this.status = newStatus;
        this.approvalScore = score;
        this.decisionReason = reason;
        if (newStatus == AuthStatus.APPROVED || newStatus == AuthStatus.DENIED) {
            this.decidedAt = Instant.now();
        }
    }

    // --- Getters (no setters: we mutate through applyDecision to keep state consistent) ---

    public Long getId() { return id; }
    public String getMemberId() { return memberId; }
    public String getProviderNpi() { return providerNpi; }
    public String getServiceCode() { return serviceCode; }
    public String getDiagnosisCode() { return diagnosisCode; }
    public int getRequestedUnits() { return requestedUnits; }
    public AuthStatus getStatus() { return status; }
    public Double getApprovalScore() { return approvalScore; }
    public String getDecisionReason() { return decisionReason; }
    public Instant getSubmittedAt() { return submittedAt; }
    public Instant getDecidedAt() { return decidedAt; }
}
