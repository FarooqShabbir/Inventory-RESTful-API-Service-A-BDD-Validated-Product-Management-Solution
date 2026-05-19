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

# GitHub URL: YOUR_GITHUB_URL_HERE/blob/main/features/products.feature
