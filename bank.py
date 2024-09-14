from account import Account, CreditCard
from datetime import datetime, timedelta, date
from utils import is_first_day_of_month, is_last_day_of_month
from config import CARD_INFO, REWARDS, FUND_INFO
import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_interest_calculation_date = None

    def create_account(self, name, password, initial_balance=0):
        if name not in self.accounts:      
            new_account = CreditCard(name, password, initial_balance)
            self.accounts[name] = new_account
            return True
        return False

    def login(self, name, password):
        account = self.accounts.get(name)
        if account is not None and account.password == password:
            return account
        return None

    def deposit(self, account, amount):
        if amount > 0:
            account.balance += amount
            return True
        return False

    def withdraw(self, account, amount):
        if 0 < amount <= account.balance:
            account.balance -= amount
            return True
        return False

    def apply_credit_card(self, account, card_type):
        account.card_type = card_type
        account.total_credit, account.interest_rate, account.points_multiplier = CARD_INFO[card_type][1:4] 
        account.available_credit = account.total_credit
        return "Application Successful"

    def get_card_description(self, card_type):
        name, limit, rate, multiplier, description = CARD_INFO[card_type]
        return description

    def spend(self, account, amount, use_credit_card=False):
        if use_credit_card == True:
            if account.card_type and amount <= account.available_credit:
                account.record_spending(amount)
                return "Spending successful with credit card"
            elif amount > account.available_credit: 
                return "Not enough credit"
            elif not account.card_type: 
                return "No credit card"
        else: 
            if amount <= account.balance: 
                account.balance -= amount
                return 'Spending successful with balance'
            else:   
                return 'Not enough balance'

    def calculate_interest(self, account, current_date):
        if account.card_type:
            if (self.last_interest_calculation_date is None or 
                self.last_interest_calculation_date.month != current_date.month):
                interest = account.unpaid_credit * (account.interest_rate / 12)
                account.unpaid_credit += interest
                account.available_credit -= interest
                self.last_interest_calculation_date = current_date
                return interest
        return 0

    def make_payment(self, account, amount):
        if account.card_type and account.unpaid_credit > 0:
            min_payment = max(account.unpaid_credit * 0.5, 10)
            if min_payment <= amount <= account.unpaid_credit:
                account.record_spending(-amount)
                account.balance -= amount
                return True
        return False

    def redeem_points(self, account, choice):
        if not account.card_type or choice not in REWARDS:
            return False
        item, points_needed = REWARDS[choice]
        if account.points >= points_needed:
            account.points -= points_needed
            return True
        return False
 
    def create_fund_account(self, account, fund_type): #have verified that fund_type is None
        account.fund_type = fund_type
        account.fund_info = FUND_INFO[fund_type]
        return True

    def fund_change(self, account):
        if account.fund_type == 'A':
            change = account.fund_balance *0.01
            account.fund_balance += change

        elif account.fund_type == 'B':
            change = account.fund_balance * random.choice([0.05, -0.05])  # random rise or fall by 5%
            account.fund_balance += change

        elif account.fund_type == 'C':
            change = account.fund_balance * random.choice([0.1, -0.1]) # random rise or fall by 10%
            account.fund_balance += change
        return change

    def invest_in_fund(self, account, amount):
        if amount <= account.balance:
            account.balance -= amount
            account.fund_balance += amount
            return True
        return False

    def withdraw_from_fund(self, account, amount):
        if amount <= account.fund_balance:
            account.fund_balance -= amount
            account.balance += amount
            return True
        return False