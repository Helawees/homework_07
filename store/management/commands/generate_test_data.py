from django.core.management.base import BaseCommand
from random import choice, uniform

from faker import Faker

from store.models import Category, Product


class Command(BaseCommand):
    """Class generates random data for classes Category and Product."""
    help = "Generate random data for classes Category and Product"

    def handle(self, *args, **kwargs):
        """Generate random data for classes Category and Product."""
        fake = Faker()

        self.stdout.write("Start generating Product categories..")
        categories = []
        cat_list = ['food', 'clothes', 'jewelry', 'hygiene', 'dishware',
                    'shoes', 'garden', 'plants', 'toys', 'tech']
        for item in cat_list:
            category = Category.objects.create(
                name=item,
                description=fake.sentence(nb_words=20))
            categories.append(category)
        self.stdout.write("10 categories have been created.")

        self.stdout.write("Start generating Product objects..")
        for i in range(10):
            product_name = f"Product n.{i + 1}"
            product_description = fake.sentence(nb_words=20)
            product_price = round(uniform(10, 100), 2)
            product_category = choice(categories)
            product = Product.objects.create(
                name=product_name,
                description=product_description,
                price=product_price,
                category=product_category)
        self.stdout.write("10 product objects have been created.")
