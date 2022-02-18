class Portfolio:
    def __init__(self):
        self.stocks = {}

    # Class method that allows to initialize the portfolio with stocks and their quantity. The stocks must be passed as a dictionary of the form {stock: quantity}.
    @classmethod
    def portfolio_with_stocks(cls, dict):
        portfolio = cls()
        for stock, quantity in dict.items():
            portfolio.add_stock(stock, quantity)
        return portfolio

    def __str__(self):
        return str(self.stocks)

    # Method to add 'quantity' of 'stock' to the portfolio. If 'quantity' is a negative number, 'quantity' of 'stock' will be removed from the portfolio.
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

    # Method that allows obtaining the annualized profit, given as a percentage, for the entire portfolio between the dates indicated. Dates must be entered as a string in the format 'YY/MM/DD'.
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


# Auxiliary function to obtain the difference of days between two dates passed as strings in 'YY/MM/DD' format
# To use this function it is necessary to import 'date' from the module 'datetime'.
def difference_in_days(date_string_1, date_string_2):
    date_1 = date.fromisoformat(date_string_1)
    date_2 = date.fromisoformat(date_string_2)
    delta = (date_2 - date_1).days
    return delta
