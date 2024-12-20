from django.db import models


class Product(models.Model):
    """
    A class representing a product.

    Attributes:
        name (str): The name of the product. Maximum length of 100 characters.
        description (str): A detailed description of the product.
        price (Decimal): The price of the product, stored as a decimal
            with a maximum of 10 digits and 2 decimal places.
        created_at (datetime): The date and time when the product was created,
            automatically set when the object is created.
        category (Category): The category to which the product belongs.
            A foreign key to the 'Category' model,
            with a cascade delete behavior.

    Methods:
        __init__(self, name, description, price, created_at, category):
        Initializes a new product object with the specified attributes.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE)


class Category(models.Model):
    """
    A class representing a product category.

    Attributes:
        name (str): The name of the category. Maximum length of 50 characters.
        description (str): A detailed description of the category.

    Methods:
        __init__(self, name, description):
        Initializes a new category object with the specified attributes.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
