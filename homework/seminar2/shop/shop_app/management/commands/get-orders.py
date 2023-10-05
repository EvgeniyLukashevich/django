from django.core.management.base import BaseCommand
from shop_app.models import Order

class Command(BaseCommand):
    help = 'Print all orders.'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            print('\n### ### ### ### ### ###\n')
            print(order)