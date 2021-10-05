# Hashing Application Automation Suite

## Running the Suite

    pip3 install -r requirements.txt
    behave

## About

Automation for the password hashing application using Behave. I chose Behave because it is a popular BDD framework and I am most familiar with automation using BDD. The application is restarted for each scenario, meaning that every scenario can be run independently of one another, and in any order. Information is passed between steps via a context object. Each time a new request is made, information about that request is stored. It also stores other information, such as the application process id.  There GitHub Actions that run the suite against Linux, macOS, and Windows on every push.

## Defects Found

- Average hashing time is not accurate
  -     features/hashing.feature:21  GET to /stats returns total requests and average time
- Hash takes 5 seconds to return a job identifier
  -     features/hashing.feature:10  POST to /hash returns job identifier immediately
- Does not handle requests made concurrently
  -     features/hashing.feature:45  The application can process multiple connections simultaneously
- Sometimes the server shuts down before sending a 200
  -     features/shutdown.feature:6  Shutdown request returns status code 200 and shuts down

## Suggestions

- Might be easier to set the port with a command line argument instead of using an environment variable
