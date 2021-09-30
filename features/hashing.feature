Feature: Password Hashing

Background:
    Given the user launches the application

Scenario: POST to /hash
    When the user makes POST request to "/hash" with password "happychimp"
    Then the user receives a job identifier

Scenario: GET to /hash
    When the user makes POST request to "/hash" with password "boredbonobo"
    And the user waits for "5" seconds
    And the user makes a GET request to "/hash" with the job identifier