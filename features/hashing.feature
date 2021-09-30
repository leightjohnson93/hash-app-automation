Feature: Password Hashing

Background:
    Given the user launches the application

Scenario: POST to /hash returns job identifier
    When the user makes a POST request to "/hash" with password "happychimp"
    Then the user receives a job identifier

Scenario: POST to /hash returns job identifier immediately
    When the user makes a POST request to "/hash" with password "moodymacaque"
    Then the user receives a response in less than "1" second

Scenario: GET to /hash returns password hash
    When the user makes a POST request to "/hash" with password "boredbonobo"
    And the user waits for "5" seconds
    And the user makes a GET request to "/hash/jobIdentifier"
    Then the user receives a base64 encoded password hash
    And the password hashing algorithm is SHA512

Scenario: GET to /stats returns requests and average time
    When the user makes "3" POST requests to "/hash"
    When the user makes a GET request to "/stats"
    Then the user receives the total number of hash requests
    And the user receives the average time of a hash request in milliseconds