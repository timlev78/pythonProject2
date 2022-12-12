class Basket:
    def __init__(self):
        self.fin_price = 0
        self.goods_list = []

    def see_basket(self):
        print(self.goods_list)

    def del_from_basket(self, amount, good_name):
        for goods in self.goods_list:
            if goods[0].name == good_name.name:
                goods[0].amount += amount
                if amount == goods[1]:
                    self.fin_price -= goods[0].price * amount
                    self.goods_list.remove(goods)
                else:
                    self.fin_price -= goods[0].price * amount
                    goods[1] -= amount

    def see_check(self):
        for goods in self.goods_list:
            print(f'{goods[0].name} x {goods[1]} = {goods[0].price * goods[1]} руб')
        print(f'ИТОГО: {self.fin_price} руб')

class Goods:
    def __init__(self, price, name, amount):
        self.price = price
        self.name = name
        self.amount = amount

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def put_in_basket(self, basket:Basket, amount):
        self.amount -= amount
        basket.goods_list += [[self, amount]]
        basket.fin_price += (self.price * amount)


class Vegetables(Goods):
    def __init__(self, price, name, mass):
        super().__init__(price, name, mass)


class Draft_drinks(Goods):
    def __init__(self, price, name, volume):
        super().__init__(price, name, volume)

cookie = Goods(79, 'Юбилейное', 500)
cucumber = Vegetables(100, 'Короткоплодные огурцы', 1000)
beer = Draft_drinks(80, 'Пиво светлое разливное', 200)

basket1 = Basket()
cookie.put_in_basket(basket1, 1)
cucumber.put_in_basket(basket1, 0.5)
beer. put_in_basket(basket1, 2)
basket1.see_basket()
basket1.del_from_basket(1, cookie)
basket1.see_basket()
basket1.del_from_basket(1, beer)
basket1.see_basket()
basket1.see_check()


