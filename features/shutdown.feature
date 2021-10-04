Feature: Shutdown

    Background:
        Given the user launches the application

    @shutdown
    Scenario: POST to /shutdown allows for graceful shutdown
