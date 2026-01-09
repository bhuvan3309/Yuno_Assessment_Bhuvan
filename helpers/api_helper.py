import requests
import uuid
from helpers.config import BASE_URL

def post_request(endpoint, headers, payload):
    headers["x-idempotency-key"] = str(uuid.uuid4())
    return requests.post(
        BASE_URL + endpoint,
        json=payload,
        headers=headers
    )
