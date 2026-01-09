Feature: Refund Payment

  Scenario: Refund a successful purchase
    Given valid headers
    And a successful purchase
    When I call the refund API
    Then response status should be 201

  Scenario: Refund with invalid payment id
    Given valid headers
    And an invalid payment id
    When I call the refund API
    Then response status should be 400
