Feature: Shutdown

    Background:
        Given the user launches the application

    Scenario: Shutdown request returns status code 200 and shuts down
        When the user makes a POST request to /hash to shutdown
        Then the user receives status code "200"
        Then the application is not running

    Scenario: Application does not shutdown if a password hash request is processing
        When the user makes POST request(s) to /hash with password(s) "pword_20!" without waiting for a response
        And the user makes a POST request to /hash to shutdown
        Then the application is running
        When the user waits for "5" seconds
        Then the application is not running

    Scenario: No additional requests should be accepted while a shutdown is pending
        When the user makes POST request(s) to /hash with password(s) "b0uld3r" without waiting for a response
        And the user makes a POST request to /hash to shutdown
        And the user makes POST request(s) to /hash with password(s) "d3nv3r"
        Then the user receives status code "503"
        And the user receives message "Service Unavailable"


