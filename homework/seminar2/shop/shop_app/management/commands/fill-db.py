from django.core.management.base import BaseCommand
from shop_app.models import Customer, Product, Order
from random import randint, choice, uniform

firstnames = [
    'James', "Ivan", "Emma", "Mary", "Stuart", "Philipp",
    'Kate', "John", "Julia", "Dennis", "Markus", "Ariana",
    'Ann', "Maria", "Christy", "Sofia", "Nickolas", "Robert",
    'Robert', 'Lisa', 'Julia', 'Frank', 'Erica', 'Steven'
]
lastnames = [
    'Wilson', 'Thuram', 'Pires', 'Hernandes', 'White', 'Gonzales',
    'Ramsey', 'Shakiri', 'Gerrard', 'Terry', 'Rooney', 'McKolmack',
    'Ballotelli', 'Benzema', 'Lahm', 'Alaba', 'Martial', 'Gates',
    'Bergkamp', 'Shaw', 'Zanetti', 'Gatusso', 'Cole', 'Viera'
]

product_first_word = [
    'Nice', 'Good', 'Perfect', 'Awesome', 'Great', 'Best',
    'White', 'Black', 'Red', 'Yellow', 'Pink', 'Blue',
    'Amazing', 'Cool', 'Violet', 'Incredible', 'Purple', 'Magenta'
]

product_second_word = [
    'Jacket', 'Jeans', 'Shirt', 'Socks', 'Sneakers', 'Hat',
    'Cap', 'Pants', 'Shorts', 'Shoes', 'Hoodie', 'Sweatshirt',
    'Coat', 'Gloves', 'Underwear', 'Glasses', 'Pillow', 'Blanket'
]


class Command(BaseCommand):
    help = 'Fill the database with fake data.'

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int, help='Number of added users.')
        parser.add_argument('number_of_products', type=int, help='Number of added products.')

    def handle(self, *args, **kwargs):
        order: Order
        number_of_users = kwargs['number_of_users']
        number_of_products = kwargs['number_of_products']
        for i in range(1, number_of_users + 1):
            firstname = choice(firstnames)
            lastname = choice(lastnames)
            customer = Customer(
                name=f'{firstname} {lastname}',
                email=f'{firstname.lower()}_{lastname.lower()}@gmail.kz',
                password=f'secret_word_#{i}',
                age=randint(16, 128)
            )
            customer.save()
        for i in range(1, number_of_products + 1):
            product = Product(
                name=f'{choice(product_first_word)} {choice(product_second_word)}',
                description=f'Long description #{i}',
                price=uniform(100, 100000),
                quantity=randint(10, 100)
            )
            product.save()
        for i in range(1, Customer.objects.count() + 1):
            if randint(0, 3):
                order = Order(client=Customer.objects.filter(pk=i).first(), total_price=0)
                order.save()
                price = 0
                for _ in range(1, randint(3, 11)):
                    product = Product.objects.filter(pk=randint(1, Product.objects.count())).first()
                    price += product.price
                    order.products.add(product)
                    product.quantity -= 1
                    product.save()
                order.total_price = price
                order.save()
