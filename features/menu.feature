Feature: Verificați funcționalitatea butonului de conectare de pe pagină

  Background:
    Given I navigate to the page

    @Menu
    Scenario Outline: User wants to navigate to the page
      When User selects the "<sign_in_button>" button
      Then I am redirected to new page "<expected_url>"
      Example:
        | sign_in_button | expected_url |