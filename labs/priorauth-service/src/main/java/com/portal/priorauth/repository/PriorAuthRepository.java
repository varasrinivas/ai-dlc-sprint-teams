package com.portal.priorauth.repository;

import com.portal.priorauth.domain.AuthStatus;
import com.portal.priorauth.domain.PriorAuthRequest;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * Data-access layer for prior auth requests.
 *
 * Spring Data JPA generates the implementation at runtime - we just declare the methods.
 * The "findByStatus" name is parsed into a query automatically.
 */
public interface PriorAuthRepository extends JpaRepository<PriorAuthRequest, Long> {

    List<PriorAuthRequest> findByStatus(AuthStatus status);
}
