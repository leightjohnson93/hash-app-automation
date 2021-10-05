import concurrent.futures
import os
from concurrent.futures import ThreadPoolExecutor

import requests
from assertpy import assert_that
from behave import *
from requests.exceptions import ReadTimeout


def get_url(path):
    return f'http://127.0.0.1:{os.getenv("PORT")}{path}'


def hash_post_request(context, password, timeout=None):
    # We can make the request and immediately continue if the timeout is set to a very low number
    try:
        response = requests.post(
            get_url("/hash"), json={"password": password}, timeout=timeout
        )
        context.hash_objects.append(
            {
                "password": password.encode("utf-8"),
                "job_identifier": response.text,
                "total_seconds": response.elapsed.total_seconds(),
            }
        )
        context.status_code = response.status_code
        context.message = response.text.strip()
    except ReadTimeout:
        pass


@when("the user makes a GET request to /stats")
def step_impl(context):
    response = requests.get(get_url("/stats"))
    context.stats["total_requests"] = response.json()["TotalRequests"]
    context.stats["average_time"] = response.json()["AverageTime"]
    context.status_code = response.status_code


@when("the user makes a GET request to /hash/jobIdentifier")
def step_impl(context):
    for hash_object in context.hash_objects:
        hash_object["hash"] = requests.get(
            get_url(f'/hash/{hash_object["job_identifier"]}')
        ).text


@when('the user makes POST request(s) to /hash with password(s) "{passwords}"')
def step_impl(context, passwords):
    for password in passwords.split(", "):
        hash_post_request(context, password)


@when(
    'the user makes POST request(s) to /hash with password(s) "{passwords}" simultaneously'
)
def step_impl(context, passwords):
    with ThreadPoolExecutor() as executor:
        futures = (
            executor.submit(hash_post_request, context, password.strip())
            for password in passwords.split(", ")
        )
        for _ in concurrent.futures.as_completed(futures):
            pass


@when(
    'the user makes POST request(s) to /hash with password(s) "{passwords}" without waiting for a response'
)
def step_impl(context, passwords):
    for password in passwords.split(", "):
        hash_post_request(context, password, 0.0000000001)


@when("the user makes a POST request to /hash to shutdown")
def step_impl(context):
    context.status_code = requests.post(get_url("/hash"), data="shutdown").status_code


@then('the user receives status code "{status_code:d}"')
def step_impl(context, status_code):
    assert_that(context.status_code).is_equal_to(status_code)


@then('the user receives a response in less than "{seconds:d}" second')
def step_impl(context, seconds):
    for hash_object in context.hash_objects:
        assert_that(hash_object["total_seconds"]).is_less_than(seconds)


@then("the user receives the total number of hash requests")
def step_impl(context):
    assert_that(context.stats["total_requests"]).is_equal_to(len(context.hash_objects))


@then("the user receives the average time of a hash request in milliseconds")
def step_impl(context):
    total_request_time = 0
    for hash_object in context.hash_objects:
        total_request_time += hash_object["total_seconds"] * 1000
    assert_that(context.stats["average_time"]).is_equal_to(
        round(total_request_time / len(context.hash_objects))
    )


@then('the user receives message "{message}"')
def step_impl(context, message):
    assert_that(context.message).is_equal_to(message)
