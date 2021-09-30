from behave import *
from assertpy import assert_that
import requests
import os
from functools import reduce
import operator
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

def get_url(path):
 return f'http://127.0.0.1:{os.getenv("PORT")}{path}'

def hash_post_request(context, path, password):
        context.responses.append(requests.post(get_url(path), json={'password': password}))

@when('the user makes a GET request to "{path}"')
def step_impl(context, path):
    if 'jobIdentifier' in path:
        path = path.replace('jobIdentifier', context.response.text)
    context.response = requests.get(get_url(path))

@when('the user makes a POST request to "{path}" with password "{password}"')
def step_impl(context, path, password):
    context.password = password
    context.response = requests.post(get_url(path), json={'password': password})
    
@when('the user makes "{request_count:d}" POST requests to "{path}"')
def step_impl(context, request_count, path):
    context.responses = []
    with ThreadPoolExecutor() as executor:
        futures = (executor.submit(hash_post_request, context, path, f'pass_{i}') for i in range(request_count))
        for i, _ in enumerate(concurrent.futures.as_completed(futures)):
            print(f'      request {i + 1} complete')
        

    context.expected_requests = request_count


@then('the user receives status code "{status_code:d}"')
def step_impl(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)

@then('the user receives a response in less than "{seconds:d}" second')
def step_impl(context, seconds):
    assert_that(context.response.elapsed.total_seconds()).is_less_than(seconds)

@then('the user receives the total number of hash requests')
def step_impl(context):
    assert_that(context.response.json()['TotalRequests']).is_equal_to(context.expected_requests)

# Round to the nearest second
@then('the user receives the average time of a hash request in milliseconds')
def step_impl(context):
    total_request_time = 0
    for response in context.responses:
        total_request_time += response.elapsed.total_seconds()
    assert_that(round(context.response.json()['AverageTime'] / 1000) * 1000).is_equal_to(round(total_request_time / len(context.responses)) * 1000)