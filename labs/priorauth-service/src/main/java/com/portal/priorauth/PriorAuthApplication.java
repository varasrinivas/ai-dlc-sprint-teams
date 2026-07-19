package com.portal.priorauth;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Entry point for the Prior Auth Portal service.
 *
 * Run it with:  mvn spring-boot:run
 * Then open:    http://localhost:8080/api/v1/prior-auth
 */
@SpringBootApplication
public class PriorAuthApplication {

    public static void main(String[] args) {
        SpringApplication.run(PriorAuthApplication.class, args);
    }
}
