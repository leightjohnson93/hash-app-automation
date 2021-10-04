Feature: Password Hashing

    Background:
        Given the user launches the application

    Scenario: POST to /hash returns job identifier
        When the user makes POST request(s) to /hash with password(s) "happychimp"
        Then the user receives a job identifier

    Scenario: POST to /hash returns job identifier immediately
        When the user makes POST request(s) to /hash with password(s) "moodymacaque"
        Then the user receives a response in less than "1" second

    Scenario: GET to /hash returns password hash
        When the user makes POST request(s) to /hash with password(s) "boredbonobo"
        And the user waits for "5" seconds
        And the user makes a GET request to /hash/jobIdentifier
        Then the user receives a base64 encoded password hash
        And the password hashing algorithm is SHA512

    Scenario: GET to /stats returns total requests and average time
        When the user makes POST request(s) to /hash with password(s) "hunter1, hunter2"
        When the user makes a GET request to /stats
        Then the user receives the total number of hash requests
        And the user receives the average time of a hash request in milliseconds

    Scenario Outline: The application can process multiple connections
        When the user makes POST request(s) to /hash with password(s) "<passwords>"
        And the user makes a GET request to /hash/jobIdentifier
        Then the password hashing algorithm is SHA512

        Examples:
            | passwords      |
            | 1_pass, 2_pass |
            | abc, def, ghi  |

    Scenario Outline: The application can process multiple connections simultaneously
        When the user makes POST request(s) to /hash with password(s) "<passwords>" simultaneously
        And the user makes a GET request to /hash/jobIdentifier
        Then the password hashing algorithm is SHA512

        Examples:
            | passwords               |
            | 1_pass, 2_pass          |
            | abc, def, ghi           |
            | birch, aspen, pine, fir |