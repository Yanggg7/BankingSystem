class Account:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

class CreditCard(Account):
    def __init__(self, name, password, initial_balance=0):
        super().__init__(name, password, initial_balance)
        self.card_type = None

        self.total_credit = 0
        self.available_credit = 0
        self.unpaid_credit = 0
        self.interest_rate = 0

        self.points = 0
        self.points_multiplier = 1
        
        self.fund_type = None
        self.fund_info = None
        self.fund_balance = 0

    def record_spending(self, amount): #call this function when spending with credit card
        self.unpaid_credit += amount
        self.available_credit -= amount
        if amount > 0:
            self.points += int(amount * self.points_multiplier)
