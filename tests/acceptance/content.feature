Feature: Test that the page have a correct content
  Scenario: Blog page has a correct title.
    Given I am on the blog page,
    Then The title is present on the blog page.
    And The title is "This is the blog page".