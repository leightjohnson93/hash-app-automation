# Hashing Application Automation Suite

## Running the Suite

    pip3 install -r requirements.txt
    behave

## About

Automation for the password hashing application using Behave. I chose Behave because it is a popular BDD framework and I am most familiar with automation using BDD. The application is restarted for each scenario, meaning that every scenario can be run independently of one another, and in any order. Information is passed between steps via a context object. Each time a new request is made, information about that request is stored. It also stores other information, such as the application process id.

## Defects Found

- Average hashing time is not accurate
- Hash takes 5 seconds to return a job identifier
- Does not handle requests made concurrently

## Suggestions

- Might be easier to set the port instead of using an environment variable
