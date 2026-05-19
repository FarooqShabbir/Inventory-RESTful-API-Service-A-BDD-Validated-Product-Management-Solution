
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product

class ProductFactory(factory.Factory):
    """ Creates fake products for testing """
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("ecommerce_name")
    category = FuzzyChoice(choices=["food", "tech", "clothing", "home"])
    available = FuzzyChoice(choices=[True, False])
    price = FuzzyDecimal(0.5, 1000.0)

    @classmethod
    def create_batch(cls, size, **kwargs):
        """ Helper to create multiple fake products """
        return super().create_batch(size, **kwargs)
