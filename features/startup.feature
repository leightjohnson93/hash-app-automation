Feature: Startup

    Scenario: Waits for HTTP connections when launched
        Given the user launches the application
        When the user makes a GET request to /stats
        Then the user receives status code "200"