import unittest
from service.models import Product, DataValidationError
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_read_a_product(self):
        """ It should Read a Product """
        product = ProductFactory()
        product.create()
        
        # Ensure the product was created with an ID
        self.assertIsNotNone(product.id)
        
        # Fetch the product back from the database
        found_product = Product.find(product.id)
        
        # Verify the data matches
        self.assertEqual(found_product.id, product.id)
        self.assertEqual(found_product.name, product.name)
        self.assertEqual(found_product.category, product.category)
        self.assertEqual(found_product.available, product.available)
        self.assertEqual(found_product.price, product.price)

# GitHub URL: YOUR_GITHUB_URL_HERE/blob/main/tests/test_models.py
