from behave import given, when, then # type: ignore
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from unique import Unique

@given('I have a list of integers {values}')
def step_given_integer_list(context, values):
    context.data = eval(values)

@given('I have a list of strings {values}')
def step_given_string_list(context, values):
    context.data = eval(values)

@given('I have an empty list')
def step_given_empty_list(context):
    context.data = []

@when('I apply the Unique iterator')
def step_when_apply_unique(context):
    context.result = list(Unique(context.data))

@when('I apply the Unique iterator with case sensitivity')
def step_when_apply_unique_case_sensitive(context):
    context.result = list(Unique(context.data, ignore_case=False))

@when('I apply the Unique iterator ignoring case')
def step_when_apply_unique_ignore_case(context):
    context.result = list(Unique(context.data, ignore_case=True))

@then('I should get values {expected}')
def step_then_check_values(context, expected):
    expected_list = eval(expected)
    assert context.result == expected_list, f"Expected {expected_list}, but got {context.result}"

@then('I should get an empty result')
def step_then_check_empty(context):
    assert context.result == [], f"Expected empty list, but got {context.result}"

@then('I should get unique values {expected}')
def step_then_check_unique_values(context, expected):
    expected_list = eval(expected)
    assert context.result == expected_list, f"Expected {expected_list}, but got {context.result}"
