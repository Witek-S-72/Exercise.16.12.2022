
class Laptop:

    DISCOUNT = 10
    lap_list = []

    def __init__ (self, name, price):
        self.name = name
        self.price = price
        Laptop.lap_list.append(self)


    def __str__ (self):
        return f'Computer of type: {self.name}, price: {self.price}'

    @staticmethod
    def to_list():
        '''display __str__ of all objects of the Laptop class'''
        for lap in Laptop.lap_list:
            print(lap)

    @staticmethod
    def calculate_discount():
        '''calculate the current price in order to all discounts provided'''
        idx = len(Laptop.lap_list)
        for id in range(idx):
            check = Laptop.lap_list[id]
            # print(check)
            print(check.__dict__)
            for k, v in check.__dict__.items():
                start_price_incl_main_discount = check.price - (check.price / 100 * Laptop.DISCOUNT)
                if k == 'discount':
                    act_price = start_price_incl_main_discount - (start_price_incl_main_discount / 100 * v)
                    return f'Name: {check.name}, start price {check.price}incl. main bonus of {Laptop.DISCOUNT+check.discount}%, current price {act_price}'
                else:
                    start_price_incl_main_discount
        return f'Name: {check.name}, start price {check.price}incl. main bonus of {Laptop.DISCOUNT}%, current price {start_price_incl_main_discount}'


lap1 = Laptop('Mac',6500)
lap2 = Laptop('Acer',4500)
lap3 = Laptop('IBM',5000)
lap3.discount = 5

print(Laptop.lap_list)

print(Laptop.calculate_discount())
