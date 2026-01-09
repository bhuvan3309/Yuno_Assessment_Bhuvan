from behave import given, when, then
from helpers.payloads import invalid_card_purchase,verify_payload, minimal_purchase, refund_payload
from helpers.api_helper import post_request
import uuid

@given("valid headers")
def step_headers(context):
    context.headers = {
        "public-api-key": "TO_BE_FILLED",
        "private-secret-key": "TO_BE_FILLED"
    }

@given("minimal purchase payload")
def step_minimal_payload(context):
    context.payload = minimal_purchase()

@given("purchase payload with invalid card")
def step_invalid_payload(context):
    context.payload = invalid_card_purchase()

@when("I call the purchase API")
def step_call_api(context):
    context.response = post_request(
        "/payments",
        context.headers,
        context.payload
    )

@then("response status should be {code:d}")
def step_validate_status(context, code):
    assert context.response.status_code == code

@given("verify payment payload")
def step_verify_payload(context):
    context.payload = verify_payload()

@given("verify payload with invalid card")
def step_verify_invalid_card(context):
    context.payload = verify_payload()
    context.payload["payment_method"]["card"]["number"] = "4000000000000002"

@when("I call the verify API")
def step_call_verify(context):
    context.response = post_request(
        "/payments",
        context.headers,
        context.payload
    )

@given("a successful purchase")
def step_successful_purchase(context):
    context.payload = minimal_purchase()
    response = post_request("/payments", context.headers, context.payload)
    context.payment_id = response.json()["id"]

@when("I call the refund API")
def step_refund(context):
    context.payload = refund_payload(context.payment_id)
    context.response = post_request(
        "/refunds",
        context.headers,
        context.payload
    )

@given("an invalid payment id")
def step_invalid_payment(context):
    context.payment_id = "invalid-id"

