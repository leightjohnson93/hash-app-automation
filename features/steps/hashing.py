from behave import *
from assertpy import assert_that
import time
import base64
import hashlib

@when('the user waits for "{seconds:d}" seconds')
def step_impl(context, seconds):
    time.sleep(seconds)

@then('the user receives a job identifier')
def step_impl(context):
    assert_that(int(context.response.text)).is_type_of(int)

# Check if base64 by decoding, re-encoding, and comparing to the original
@then('the user receives a base64 encoded password hash')
def step_impl(context):
    b64_hash = b64_hash = context.response.text
    assert_that(b64_hash).is_equal_to(base64.b64encode(base64.b64decode(b64_hash)).decode())

@then('the password hashing algorithm is SHA512')
def step_impl(context):
    assert_that(base64.b64decode(context.response.text)).is_equal_to(hashlib.sha512(context.password.encode("utf-8")).digest())