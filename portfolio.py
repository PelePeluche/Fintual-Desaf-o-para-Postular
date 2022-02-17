from datetime import date


# Clase creada para probar Portfolio y sus métodos
class Stock:
    def __init__(self):
        self.valores = {date(2020, 3, 12): 5, date(2022, 4, 12): 7}

    def add_valor(self, date, price):
        self.valores[date] = price

    def price(self, date_string):
        date_parsed = date.fromisoformat(date_string)
        return self.valores[date_parsed]


# Función auxiliar que sirve para obtener la diferencia de días entre dos fechas pasadas como strings en formato 'YY/MM/DD'
def difference_in_days(date_string_1, date_string_2):
    date_1 = date.fromisoformat(date_string_1)
    date_2 = date.fromisoformat(date_string_2)
    delta = (date_2 - date_1).days
    return delta


class Portfolio:
    def __init__(self, **kwargs):
        self.stocks = {}
        for stock, quantity in kwargs.items():
            self.add_stock(stock, quantity)

    def __str__(self):
        return str(self.stocks)

    def add_stock(self, stock, quantity):
        self.stocks[stock] = self.stocks.get(stock, 0) + quantity

    def remove_stock(self, stock, quantity):
        self.stocks[stock] -= quantity

    def profit(self, date_string_1, date_string_2):
        profit = 0
        initial_investment = 0
        days = difference_in_days(date_string_1, date_string_2)
        for stock in self.stocks:
            initial_investment += stock.price(date_string_1) * self.stocks[stock]
            profit += (
                stock.price(date_string_2) - stock.price(date_string_1)
            ) * self.stocks[stock]
        simple_profit = profit / initial_investment
        annualized_profit = (simple_profit ** (365 / days) - 1) * 100
        return annualized_profit
