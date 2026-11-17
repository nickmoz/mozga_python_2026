from datetime import datetime


class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = 0
        self.set_price(price)

    def __str__(self):
        return f'{self.name}: ${self.price}'

    def set_price(self, price):
        if price < 0:
            print(
                f'ERROR: invalid price {price}. Please enter a non-negative value.')
            self.price = 0
        else:
            self.price = price


class Menu:
    def __init__(self):
        self.beverages = {}

    def add_beverage(self, name, price):
        if name in self.beverages:
            print(f'{name} already in menu')
        else:
            b = Beverage(name, price)
            self.beverage[name] = b

    def display_menu(self):
        for key in self.beverages:
            beverage = self.beverages[key]
            print(beverage)


class OrderItem:
    def __init__(self, beverage, quantity):
        self.beverage = beverage
        self.quantity = 1

    def set_quantity(self, quantity):
        if quantity < 1:
            print(f'Invalid quantity')
        else:
            self.quantity = quantity

    def __str__(self):
        return f'{self.beverage.name}: {self.quantity}'


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.date.time = datetime.now()
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class CoffeeShop:
    def __init__(self):
        self.menu = Menu()
        self.menu.add_beverage('')
        self.orders = []

    def display_app_menu(self):
        print('1. Add Order')
        print('2. Orders by Beverage')
        print('3. Orders by Customer')
        print('0. Exit')

    def select_from_app_menu(self):
        choice = int(input('Select: '))
        if choice == 1:
            print('add order')
        elif choice == 2:
            print('orders by beverage')
        elif choice == 3:
            print('orders by customer')
        elif choice == 0:
            print('exit')
        return choice

    def add_order(self):
        print('==== ADD ORDER ====')
        customer = input('Customer: ')
        order = Order(customer)
        cont = 'y'
        while cont == 'y':
            self.menu.display_menu()
            beverage = input('Beverage: ')
            quantity = int(input('Quantity: '))

            order.add_item(OrderItem(beverage, quantity))
            cont = input('Continue? y/n: ')
