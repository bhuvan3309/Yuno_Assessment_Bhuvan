Feature: Purchase Payment

  Scenario: Purchase with minimal fields
    Given valid headers
    And minimal purchase payload
    When I call the purchase API
    Then response status should be 201

  Scenario: Purchase with invalid card
    Given valid headers
    And purchase payload with invalid card
    When I call the purchase API
    Then response status should be 400
