Feature: Startup

    Background:
        Given the user launches the application

    Scenario: Process is started when launched
        Then the application is running

    Scenario: Waits for HTTP connections when launched
        When the user makes a GET request to /stats
        Then the user receives status code "200"