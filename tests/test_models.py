import unittest
from service.models import Product, DataValidationError
from tests.factories import ProductFactory

#READ
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

#Update
class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_update_a_product(self):
        """ It should Update a Product """
        product = ProductFactory()
        product.create()
        self.assertIsNotNone(product.id)
        
        # Change an attribute
        product.name = "Updated Name"
        original_id = product.id
        product.update()
        
        # Fetch it back and verify the change
        found_product = Product.find(original_id)
        self.assertEqual(found_product.name, "Updated Name")
        self.assertEqual(found_product.id, original_id)

#Delete
class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_delete_a_product(self):
        """ It should Delete a Product """
        product = ProductFactory()
        product.create()
        self.assertIsNotNone(product.id)
        
        # Verify the product exists before deletion
        products = Product.all()
        self.assertEqual(len(products), 1)
        
        # Delete the product
        product.delete()
        
        # Verify the product is gone
        products = Product.all()
        self.assertEqual(len(products), 0)

#list all
class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_list_all_products(self):
        """ It should list all Products in the database """
        # 1. Create a set of products
        for _ in range(5):
            ProductFactory().create()
        
        # 2. Fetch all products
        products = Product.all()
        
        # 3. Verify the count matches
        self.assertEqual(len(products), 5)


#find by name
class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_find_by_name(self):
        """ It should Find a Product by Name """
        # 1. Create a set of products
        ProductFactory(name="Apple").create()
        ProductFactory(name="Banana").create()
        
        # 2. Search for one of them
        products = Product.find_by_name("Apple")
        
        # 3. Verify results
        self.assertEqual(products[0].name, "Apple")
        self.assertEqual(len(products), 1)


#find by category
class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_find_by_category(self):
        """ It should Find Products by Category """
        # 1. Create a set of products with different categories
        ProductFactory(category="food").create()
        ProductFactory(category="tech").create()
        ProductFactory(category="food").create()
        
        # 2. Search for products in the 'food' category
        products = Product.find_by_category("food")
        
        # 3. Verify results
        self.assertEqual(len(products), 2)
        for product in products:
            self.assertEqual(product.category, "food")


#find by availability

class TestProductModel(unittest.TestCase):
    """ Test cases for Product Model """

    def test_find_by_availability(self):
        """ It should Find Products by Availability """
        # 1. Create a set of products with mixed availability
        ProductFactory(available=True).create()
        ProductFactory(available=False).create()
        ProductFactory(available=True).create()
        
        # 2. Search for products that are available (True)
        products = Product.find_by_availability(True)
        
        # 3. Verify results
        self.assertEqual(len(products), 2)
        for product in products:
            self.assertTrue(product.available)

