Feature: Test that the page have a correct content
  Scenario: Blog page has a correct title.
    Given I am on the blog page,
    Then The title is present on the page.
    And The title is "This is the blog page".

  Scenario: Homepage has a correct title.
    Given I am on the homepage,
    Then The title is present on the page.
    And The title is "This is the homepage".

  Scenario: Blog page loads the posts
    Given I am on the blog page.
    And I wait for the post to load
    Then The post section is present on the page

  Scenario: User can create new posts
    Given I am on the new post page.
    When Enter "New-Post" into the "title" field.
    And Enter "New-content" into the "content" field.
    And Press submit button.
    Given I am on the blog page.
    Given I wait for the post to load
    Then The new post title is "New-post"