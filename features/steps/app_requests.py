from behave import *
from assertpy import assert_that
import requests
import os

@when('the user makes a GET request to "{path}"')
def step_impl(context, path):
    url = f'http://127.0.0.1:{os.getenv("PORT")}{path}'
    context.response = requests.get(url)

@Then('the user receives status code "{status_code:d}"')
def step_impl(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)