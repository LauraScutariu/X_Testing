Feature: Login to the account successfully

  @SignIn
  Scenario: Sign in with an account
    When I access the "Sign In" button
    When Enter a valid email address
    When Enter a valid password
    Then Login to the account successfully.