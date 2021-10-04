from behave import *
from assertpy import assert_that, fail
import time
import base64
import hashlib


@when('the user waits for "{seconds:d}" seconds')
def step_impl(_, seconds):
    time.sleep(seconds)


@then('the user receives a job identifier')
def step_impl(context):
    for hash_object in context.hash_objects:
        job_identifier = hash_object['job_identifier']
        try:
            int(job_identifier)
        except Exception:
            fail(f'expected {job_identifier} to be an integer')


@then('the user receives a base64 encoded password hash')
def step_impl(context):
    for hash_object in context.hash_objects:
        hash = hash_object['hash']
        # Check if base64 by decoding, re-encoding, and comparing to the original
        assert_that(hash).is_equal_to(
            base64.b64encode(base64.b64decode(hash)).decode())


@then('the password hashing algorithm is SHA512')
def step_impl(context):
    for hash_object in context.hash_objects:
        assert_that(base64.b64decode(hash_object['hash'])).is_equal_to(
            hashlib.sha512(hash_object['password']).digest())
