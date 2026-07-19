package com.portal.priorauth.web;

import com.portal.priorauth.domain.AuthStatus;
import com.portal.priorauth.domain.PriorAuthRequest;
import com.portal.priorauth.service.PriorAuthService;
import com.portal.priorauth.web.dto.AuthResponse;
import com.portal.priorauth.web.dto.DecisionRequest;
import com.portal.priorauth.web.dto.SubmitAuthRequest;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * REST API for the Prior Auth Portal.
 *
 * Base path: /api/v1/prior-auth
 *
 * Endpoints:
 *   POST   /                     submit a new request (auto-scored)
 *   GET    /{id}                 fetch one request
 *   GET    /?status=PENDING_REVIEW   list requests, optionally filtered by status
 *   POST   /{id}/decision        a reviewer approves or denies a pending request
 *
 * NOTE: There is intentionally no "appeals" endpoint yet. Adding one is a course lab.
 */
@RestController
@RequestMapping("/api/v1/prior-auth")
public class PriorAuthController {

    private final PriorAuthService service;

    public PriorAuthController(PriorAuthService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<AuthResponse> submit(@Valid @RequestBody SubmitAuthRequest body) {
        PriorAuthRequest saved = service.submit(
                body.memberId(),
                body.providerNpi(),
                body.serviceCode(),
                body.diagnosisCode(),
                body.requestedUnits());
        return ResponseEntity.status(HttpStatus.CREATED).body(AuthResponse.from(saved));
    }

    @GetMapping("/{id}")
    public AuthResponse getOne(@PathVariable Long id) {
        return AuthResponse.from(service.getById(id));
    }

    @GetMapping
    public List<AuthResponse> list(@RequestParam(required = false) AuthStatus status) {
        return service.list(status).stream()
                .map(AuthResponse::from)
                .toList();
    }

    @PostMapping("/{id}/decision")
    public AuthResponse decide(@PathVariable Long id, @Valid @RequestBody DecisionRequest body) {
        return AuthResponse.from(service.decide(id, body.decision(), body.reason()));
    }
}
