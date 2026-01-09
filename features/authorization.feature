Feature: Card Authorization API

  As a merchant
  I want to authorize a card payment
  So that I can capture or cancel it later

  Background:
    Given the API is available
    And the workflow is "DIRECT"

  # POSITIVE SCENARIOS

  @sanity @authorization
  Scenario: Authorize payment with minimal required fields
    When I create an authorization payment with minimal fields
    Then the response status code should be 201
    And the authorization status should be "AUTHORIZED"

  @regression @authorization
  Scenario: Authorize payment with all fields
    When I create an authorization payment with all fields
    Then the response status code should be 201
    And the authorization status should be "AUTHORIZED"

  # NEGATIVE SCENARIOS

  @negative @authorization
  Scenario: Authorization fails with invalid card number
    When I create an authorization payment with an invalid card number
    Then the response status code should be 400
    And the error message should be returned

  @negative @authorization
  Scenario: Authorization fails when workflow is missing
    When I create an authorization payment without workflow
    Then the response status code should be 400
    And the error message should be returned
