class BankText:
    DEPOSIT_SUCCESS = "Deposit successful. Current balance: ${balance:.2f}"
    DEPOSIT_FAILURE = "Deposit failed. Please ensure the amount is greater than 0."
    WITHDRAW_SUCCESS = "Withdrawal successful. Current balance: ${balance:.2f}"
    WITHDRAW_FAILURE = "Withdrawal failed. Please ensure sufficient balance and valid withdrawal amount."
    NOT_FIRST_DAY = "You can only apply for a credit card on the first day of each month."
    NOT_LAST_DAY = "Credit card payments can only be made on the last day of each month."
    BALANCE = "Current balance: ${balance:.2f}"
    NO_CREDIT_CARD = "You don't have a credit card yet."
    CREDIT_CARD_INFO = """Your {card_name} information \n Total limit: ${total_credit:.2f} \n  Annual interest rate: {interest_rate:.1f}% \n Available credit: ${available_credit:.2f}\n Unpaid balance: ${unpaid_credit:.2f} \n Current points: {points}"""
    SPEND_SUCCESS_CREDIT = """Successfully spent ${amount}
Credit card available balance: ${available_credit:.2f}
Points earned from this transaction: {points_earned}
Total current points: {total_points}"""
    SPEND_SUCCESS_DEBIT = "Successfully spent ${amount}\nAccount balance: ${balance:.2f}"
    SPEND_FAILURE = "Transaction failed. Please check your balance or credit card limit."
    PAYMENT_INFO = "Unpaid balance: ${unpaid_credit:.2f}\nMinimum payment: ${min_payment:.2f}"
    NO_PAYMENT_NEEDED = "You don't have any credit card that needs payment."
    PAYMENT_FAILURE_MIN = "Payment failed. The minimum payment is ${min_payment:.2f}. Please pay at least this amount."
    PAYMENT_FAILURE_EXCESS = "Payment failed. The unpaid balance is ${unpaid_credit:.2f}. No need to pay more."
    PAYMENT_SUCCESS = "Payment successful! Paid amount: ${amount:.2f}."
    PAYMENT_FAILURE_NO_CARD = "Payment failed. You don't have a credit card or there's no need for payment."
    REWARDS_HEADER = "Available rewards:"
    REWARDS_ITEM = "| {key}. {item:<10} | {points:>6} points |"
    NO_CREDIT_CARD_POINTS = "You don't have a credit card. Unable to redeem points."
    INVALID_REWARD_CHOICE = "Invalid choice. Please try again."
    REDEEM_SUCCESS = "Congratulations! Successfully redeemed {item}.\nRemaining points: {points}"
    REDEEM_FAILURE = "Insufficient points. You currently have {current_points} points, but need {required_points} points to redeem {item}."
    REDEEM_CANCELLED = "You cancelled the redemption."


    FUND_ACCOUNT_INFO = "Fund Name: {fund_name}\nFund Balance: {fund_balance}\n"
    FUND_CREATION_CONFIRMATION = "All investments carry risk. Please invest wisely.\n\nConfirm creation of this fund?"

    NO_FUND_ACCOUNT = "You do not have a fund account."