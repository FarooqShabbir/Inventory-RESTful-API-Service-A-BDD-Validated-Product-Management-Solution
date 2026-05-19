from behave import given
import requests

@given('the following products exist')
def step_impl(context):
    """ Load products into the database via REST API """
    # Define the base URL of the running test server
    base_url = "http://localhost:8080/products"
    
    # Iterate through the table in the Gherkin feature file
    for row in context.table:
        payload = {
            "name": row["name"],
            "category": row["category"],
            "available": row["available"] == "True",
            "price": float(row["price"])
        }
        
        # Post the product to the API
        response = requests.post(base_url, json=payload)
        
        # Verify the product was created successfully
        assert response.status_code == 201, f"Failed to create product: {row['name']}"

