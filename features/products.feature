Feature: The product service under test
    As a user
    I want to be able to read product information
    So that I can verify product details

    Background:
        Given the following products exist
            | name   | category | available | price |
            | Apple  | food     | True      | 1.50  |
            | Banana | food     | True      | 0.75  |

    Scenario: Read a single product
        When I retrieve the product with name "Apple"
        Then I should see "Apple" in the results
        And I should not see "Banana" in the results

    Scenario: Update a Product
        When I search for "Apple"
        Then I should see "Apple" in the results
        When I change "Apple" to "Red Apple" and press "Update"
        Then I should see "Success"
        When I retrieve the product with ID from "Red Apple"
        Then the "name" field should be "Red Apple"

    Scenario: Delete a Product
        When I search for "Apple"
        Then I should see "Apple" in the results
        When I delete "Apple"
        Then I should see "Product has been Deleted!"
        When I search for "Apple"
        Then I should not see "Apple" in the results

    Scenario: List all Products
        When I press "Clear"
        And I press "Search"
        Then I should see "Success"
        And I should see "Hat" in the results
        And I should see "Shoes" in the results

    Scenario: Search for a Product by Category
        When I press "Clear"
        And I select "Food" in the category dropdown
        And I press "Search"
        Then I should see "Big Mac" in the results
        And I should not see "Shoes" in the results

    Scenario: Search for a Product by Availability
        When I press "Clear"
        And I select "True" in the available dropdown
        And I press "Search"
        Then I should see "Success"
        And I should see available items in the results
        And I should not see unavailable items

    Scenario: Search for a Product by Name
        When I press "Clear"
        And I fill in "Name" with "Apple"
        And I press "Search"
        Then I should see "Success"
        And I should see "Apple" in the results
