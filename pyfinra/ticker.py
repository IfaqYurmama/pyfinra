from . import quote
from .financials import balance_sheet, inc_statement

class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def quote(self):
        return quote.quote(self.ticker)

    def financials_balancesheet(self):
        return balance_sheet.balance_sheet(self.ticker,self.quote()["exchange"])