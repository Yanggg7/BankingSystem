from datetime import datetime

# GUI settings
GUI_TITLE = "Bank Account Management System"
GUI_GEOMETRY = "700x600"
GUI_FONT = "Helvetica 12"

# Initial date
INITIAL_DATE = datetime(2024, 1, 1)

# Frame titles
FRAME_TITLES = {
    "basic": "Basic Functions",
    "credit": "Credit Card Functions",
    "investment": "Investment Functions",
    "time": "Time Functions"
}

# Button configurations
BUTTON_CONFIG = {
    "basic": [
        ("Deposit", "deposit"),
        ("Withdraw", "withdraw"),
        ("Check Balance", "get_balance"),
        ("Spend", "spend")
    ],
    "credit": [
        ("Apply for Credit Card", "apply_credit_card"),
        ("View Credit Card Info", "get_credit_card"),
        ("Credit Card Payment", "make_payment"),
        ("Redeem Points", "redeem_points")
    ],
    "investment": [
        ("Create Fund Account", "create_fund_account"),
        ("View Fund Account", "get_fund_account"),
        ("Invest in Fund", "invest_fund"),
        ("Withdraw from Fund", "withdraw_fund")
    ],
    "time": [  # Changed from "debug" to "time"
        ("Next Day", 1),
        ("Next 10 Days", 10),
        ("Next Month", 30)
    ]
}

REWARDS = {
    1: ("Movie Ticket", 1000),
    2: ("Coffee Maker", 5000),
    3: ("Headphones", 10000),
    4: ("Smartphone", 30000),
    5: ("Refrigerator", 50000),
    6: ("Laptop", 100000)
}

CARD_INFO = {
    'A': ['Basic Card', 5000, 0.12, 1, """
--------------------- Basic Card ---------------------\n
Introduction: The Basic Card is suitable for first-time credit card users.\n
Interest Rate: 12% annual interest rate\n
Credit Limit: $5,000\n
Earn 1 point for every $1 spent\n
--------------------- Basic Card ---------------------
"""],
    'B': ['Rewards Card', 10000, 0.24, 3, """
--------------------- Rewards Card ---------------------\n
Introduction: The Rewards Card is ideal for users who like to accumulate rewards through daily spending.\n
Interest Rate: 24% annual interest rate\n
Credit Limit: Up to $10,000\n
Earn 3 points for every $1 spent\n
--------------------- Rewards Card ---------------------
"""],
    'C': ['Premium Card', 25000, 0.36, 5, """
--------------------- Premium Card ---------------------\n
Introduction: The Premium Card is suitable for high-end users, offering luxury services and premium reward mechanisms.\n
Interest Rate: 36% annual interest rate\n
Credit Limit: $25,000\n
Earn 5 points for every $1 spent\n
--------------------- Premium Card ---------------------
"""]
}



FUND_INFO= {
    'A':['Conservative Fund', 'Low risk, Low return'],
    'B':['Balanced Fund', 'Decent returns with a relatively stable risk.'],
    'C':['Aggressive Fund', 'For those who are not afraid to aim for the stars']
}