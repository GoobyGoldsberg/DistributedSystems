class InvestmentStrategy():
    def buyStock(self, amount, current_price):
        pass


class Aggressive(InvestmentStrategy):
    def buyStock(self, amount, current_price):
        current_price = current_price
        return f'{amount} has been invested at the price of {current_price}'
    
    
class Passive(InvestmentStrategy):
    def buyStock(self, amount, current_price):
        amount = amount / 2
        current_price = (current_price / 100) * 90
        return f'{amount} will be invested when the price is equal to {current_price}'
        
    
    
class StockBuyer:
    def __init__(self, strategy):
         self.strategy = strategy
         
    def set_strategy(self, strategy):
        self.strategy = strategy
        
    def buyStock(self, amount, current_price):
        return self.strategy.buyStock(amount, current_price)
    

aggr = Aggressive()
passi = Passive()

stock_buyer = StockBuyer(aggr)

aggr_result = stock_buyer.buyStock(2000, 120)

print(aggr_result)

stock_buyer.set_strategy(passi)

passi_result = stock_buyer.buyStock(1500, 100)

print(passi_result)