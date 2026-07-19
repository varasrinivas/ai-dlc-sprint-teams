package com.portal.priorauth.domain;

/**
 * The lifecycle of a prior authorization request.
 *
 * SUBMITTED       -> just received, not yet scored
 * APPROVED        -> auto-approved by the rules engine, or approved by a reviewer
 * PENDING_REVIEW  -> the rules engine wasn't confident enough; a human must decide
 * DENIED          -> denied by a reviewer
 */
public enum AuthStatus {
    SUBMITTED,
    APPROVED,
    PENDING_REVIEW,
    DENIED
}
