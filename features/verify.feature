Feature: Verify Card Payment

  Scenario: Verify card with valid details
    Given valid headers
    And verify payment payload
    When I call the verify API
    Then response status should be 201

  Scenario: Verify card with invalid card number
    Given valid headers
    And verify payload with invalid card
    When I call the verify API
    Then response status should be 400
