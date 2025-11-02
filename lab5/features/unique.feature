Feature:
  Scenario: Remove duplicates from integer list
    Given I have a list of integers [1, 1, 2, 2, 3, 3]
    When I apply the Unique iterator
    Then I should get unique values [1, 2, 3]

  Scenario: Process strings with case sensitivity
    Given I have a list of strings ["a", "A", "b", "B", "a"]
    When I apply the Unique iterator with case sensitivity
    Then I should get values ["a", "A", "b", "B"]

  Scenario: Process strings ignoring case
    Given I have a list of strings ["a", "A", "b", "B", "a"]
    When I apply the Unique iterator ignoring case
    Then I should get values ["a", "b"]

  Scenario: Handle empty input
    Given I have an empty list
    When I apply the Unique iterator
    Then I should get an empty result

  Scenario: Preserve insertion order
    Given I have a list of integers [3, 1, 2, 1, 3, 4]
    When I apply the Unique iterator
    Then I should get values [3, 1, 2, 4]
