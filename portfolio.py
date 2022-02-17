"""Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. 
Assume each Stock has a "Price" method that receives a date and returns its price.
Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates."""

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


# Auxiliary function to obtain the difference of days between two dates passed as strings in 'YY/MM/DD' format
def difference_in_days(date_string_1, date_string_2):
    date_1 = date.fromisoformat(date_string_1)
    date_2 = date.fromisoformat(date_string_2)
    delta = (date_2 - date_1).days
    return delta


class Portfolio:
    def __init__(self):
        self.stocks = {}

    @classmethod
    def portfolio_with_stocks(cls, dict):
        portfolio = cls()
        for stock, quantity in dict.items():
            portfolio.add_stock(stock, quantity)
        return portfolio

    def __str__(self):
        return str(self.stocks)

    def add_stock(self, stock, quantity):
        if type(stock) != Stock or type(quantity) != int:
            print("The input types are not correct")
        else:
            if quantity >= 0:
                self.stocks[stock] = self.stocks.get(stock, 0) + quantity
            else:
                try:
                    if self.stocks[stock] >= quantity:
                        self.stocks[stock] -= quantity
                    else:
                        print("You don't have that many stocks")
                except KeyError:
                    print("There is no such stock in the portfolio")
                except NameError:
                    print("There is no such stock")

    def profit(self, date_string_1, date_string_2):
        profit = 0
        initial_investment = 0
        days = difference_in_days(date_string_1, date_string_2)
        for stock in self.stocks:
            try:
                initial_investment += stock.price(date_string_1)
                profit += stock.price(date_string_2) - stock.price(date_string_1)
            except:
                print(
                    "There is a problem in obtaining the price for this stock: ",
                    stock,
                )
        try:
            simple_profit = profit / initial_investment
            annualized_profit = ((1 + simple_profit) ** (365 / days) - 1) * 100
            return annualized_profit
        except ZeroDivisionError:
            print("No initial investment on the date indicated")
