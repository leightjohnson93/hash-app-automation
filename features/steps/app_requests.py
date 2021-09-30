from behave import *
from assertpy import assert_that
import requests
import os

def get_url(path):
 return f'http://127.0.0.1:{os.getenv("PORT")}{path}'

@when('the user makes a GET request to "{path}"')
def step_impl(context, path):
    context.response = requests.get(get_url(path))

@when('the user makes POST request to "{path}" with password "{password}"')
def step_impl(context, path, password):
    context.response = requests.post(get_url(path), json={'password': password})

@Then('the user receives status code "{status_code:d}"')
def step_impl(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)

@Then('the user receives a job identifier')
def step_impl(context):
    assert_that(int(context.response.text)).is_type_of(int)