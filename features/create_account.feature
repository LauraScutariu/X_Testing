Feature: Successfully creating an account

  Background:
    Given The user navigates to main page - "create account" button

  @CreateAccount
  Scenario: Create a new user account
    When I access the "create account" button
    When Enter a real name
    When Enter a valid email address
    When Enter the date of birth
    When Select the "next" button(step 1)
    When I describe my experience in step 2
    When I check the information from step 1
    When I verify my email address by receiving a verification code
    Then Account created successfully.