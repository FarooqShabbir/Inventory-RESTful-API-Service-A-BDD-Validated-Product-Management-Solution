import unittest
from service import app
from tests.factories import ProductFactory

#read
class TestProductRoutes(unittest.TestCase):
    """ Test cases for Product Routes """

    def setUp(self):
        self.app = app.test_client()

    def test_get_product(self):
        """ It should Get a single Product """
        # 1. Create a test product
        product = ProductFactory()
        product.create()
        
        # 2. Make the GET request
        resp = self.app.get(f"/products/{product.id}")
        
        # 3. Verify the response
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], product.name)
        self.assertEqual(data["id"], product.id)


import unittest
from service import app
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    #update
    def test_update_product(self):
        """ It should Update an existing Product """
        product = ProductFactory()
        product.create()
        product.name = "New Name"
        resp = self.app.put(f"/products/{product.id}", json=product.serialize())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["name"], "New Name")

    #delete
    def test_delete_product(self):
        """ It should Delete a Product """
        product = ProductFactory()
        product.create()
        resp = self.app.delete(f"/products/{product.id}")
        self.assertEqual(resp.status_code, 204)

    #list all
    def test_list_all_products(self):
        """ It should List all Products """
        ProductFactory().create()
        ProductFactory().create()
        resp = self.app.get("/products")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.get_json()), 2)

    #list by name
    def test_list_by_name(self):
        """ It should List Products by Name """
        ProductFactory(name="Apple").create()
        resp = self.app.get("/products", query_string="name=Apple")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()[0]["name"], "Apple")

    #list by category
    def test_list_by_category(self):
        """ It should List Products by Category """
        ProductFactory(category="food").create()
        resp = self.app.get("/products", query_string="category=food")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()[0]["category"], "food")

    #list by availability
    def test_list_by_availability(self):
        """ It should List Products by Availability """
        ProductFactory(available=True).create()
        resp = self.app.get("/products", query_string="available=True")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.get_json()[0]["available"])

