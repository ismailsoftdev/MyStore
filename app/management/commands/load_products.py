import json
from django.core.management.base import BaseCommand
from app.models import Product

class Command(BaseCommand):
    help = 'Load sample products from a JSON file into the Product model'

    def handle(self, *args, **kwargs):
        file_path = 'products.json'  # Adjust the path if necessary

        try:
            with open(file_path, 'r') as file:
                products = json.load(file)

            for product_data in products:
                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    defaults={
                        'description': product_data['description'],
                        'price': product_data['price'],
                        'image': product_data.get('image', None),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Product '{product.name}' created."))
                else:
                    self.stdout.write(f"Product '{product.name}' already exists.")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
