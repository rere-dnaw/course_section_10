Feature: Test navigation between
  all pages.

  Scenario: Homepage can go to Blog
    Given I am on the homepage.
    When  I press the link "Go to blog"
    Then  I am on the blog page.

  Scenario: Blog can go to Homepage
    Given I am on the blog page.
    When  I press the link "Go to home"
    Then  I am on the homepage.