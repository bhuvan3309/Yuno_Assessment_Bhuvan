def minimal_purchase():
    return {
        "account_id": "ACCOUNT_ID",
        "amount": 1000,
        "currency": "USD",
        "workflow": "DIRECT",
        "payment_method": {
            "type": "CARD",
            "card": {
                "number": "4111111111111111",
                "expiration_month": "12",
                "expiration_year": "2030",
                "cvv": "123"
            }
        }
    }

def invalid_card_purchase():
    payload = minimal_purchase()
    payload["payment_method"]["card"]["number"] = "4000000000000002"
    return payload

def verify_payload():
    payload = minimal_purchase()
    payload["verify"] = True
    return payload

def refund_payload(payment_id):
    return {
        "payment_id": payment_id,
        "amount": 1000
    }
