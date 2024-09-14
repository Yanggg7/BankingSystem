import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, StringVar
from bank import Bank
from datetime import datetime, timedelta
from utils import is_first_day_of_month, is_last_day_of_month
from Text import BankText
from config import CARD_INFO, REWARDS, FUND_INFO, FRAME_TITLES, BUTTON_CONFIG  

class BankGUI:
    def __init__(self, master):
        self.master = master
        self.bank = Bank()
        self.master.title("MH6803-B Bank Account Management System")
        self.master.geometry("700x500")
        
        self.master.iconbitmap('')
        
        self.master.option_add('*Dialog.msg.font', 'Helvetica 14')
        
        self.current_date = datetime(2024, 1, 1)
        self.current_account = None
        self.init_ui()

    def init_ui(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.welcome_label = tk.Label(self.main_frame, text="Welcome to the Banking System", font=("Times New Roman", 20))
        self.welcome_label.pack(pady=20)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        button_width = 20
        button_height = 2
        button_font = ("Helvetica", 15)

        tk.Button(self.button_frame, text="Login", command=lambda: self.show_frame("login"), 
                  width=button_width, height=button_height, font=button_font).pack(pady=10)
        tk.Button(self.button_frame, text="Create Account", command=lambda: self.show_frame("create"), 
                  width=button_width, height=button_height, font=button_font).pack(pady=10)
        tk.Button(self.button_frame, text="Quit", command=self.master.quit, 
                  width=button_width, height=button_height, font=button_font).pack(pady=10)

        self.login_frame = self.create_login_frame()
        self.create_account_frame = self.create_account_frame()
        self.account_frame = tk.Frame(self.main_frame)
        self.Main_Menu()

        # Create a bottom frame for labels
        bottom_frame = tk.Frame(self.main_frame)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Add group information label (left bottom corner)
        tk.Label(bottom_frame, text="MH6803-B Group14", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5, pady=5)

        # Create version label (right bottom corner)
        tk.Label(bottom_frame, text=f"Beta 1.0", font=("Helvetica", 12)).pack(side=tk.RIGHT, padx=5, pady=5)

        # Initially show main frame
        self.show_frame("main")

    def Main_Menu(self):
        # Create a frame to hold the top two frames side by side
        top_frame = tk.Frame(self.account_frame)
        top_frame.pack(fill=tk.X, padx=5, pady=5)

        # Create the first two frames side by side
        for frame_name in ["basic", "credit"]:
            frame = tk.LabelFrame(top_frame, text=FRAME_TITLES[frame_name])
            frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            setattr(self, f"{frame_name}_frame", frame)

            for text, command in BUTTON_CONFIG[frame_name]:
                tk.Button(frame, text=text, command=getattr(self, command)).pack(fill=tk.X, pady=2)

        # Create the investment frame below, spanning the full width
        inv_frame = tk.LabelFrame(self.account_frame, text=FRAME_TITLES["investment"])
        inv_frame.pack(fill=tk.X, padx=5, pady=5)
        setattr(self, "investment_frame", inv_frame)

        # Create a frame to hold investment buttons horizontally
        inv_button_frame = tk.Frame(inv_frame)
        inv_button_frame.pack(fill=tk.X)

        for text, command in BUTTON_CONFIG["investment"]:
            tk.Button(inv_button_frame, text=text, command=getattr(self, command)).pack(side=tk.LEFT, padx=2, pady=2, expand=True)

        # Create the time frame
        time_frame = tk.LabelFrame(self.account_frame, text=FRAME_TITLES["time"])
        time_frame.pack(fill=tk.X, padx=5, pady=5)
        setattr(self, "time_frame", time_frame)

        self.date_label = tk.Label(time_frame, text="")
        self.date_label.pack(pady=5)

        # Create a frame to hold time buttons horizontally
        time_button_frame = tk.Frame(time_frame)
        time_button_frame.pack(fill=tk.X)

        for text, days in BUTTON_CONFIG["time"]:
            tk.Button(time_button_frame, text=text, command=lambda d=days: self.update_date(d)).pack(side=tk.LEFT, padx=2, pady=2, expand=True)

        # Logout button
        tk.Button(self.account_frame, text="Logout", command=self.logout).pack(fill=tk.X, pady=10)

    def create_login_frame(self):
        frame = tk.Frame(self.main_frame)
        tk.Label(frame, text="Username:").pack()
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack()
        tk.Label(frame, text="Password:").pack()
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack()
        tk.Button(frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(frame, text="Back", command=lambda: self.show_frame("main")).pack()
        return frame

    def create_account_frame(self):
        frame = tk.Frame(self.main_frame)
        tk.Label(frame, text="New Username:").pack()
        self.new_username_entry = tk.Entry(frame, highlightthickness=1, highlightcolor='black',)
        self.new_username_entry.pack()
        tk.Label(frame, text="New Password:").pack()
        self.new_password_entry = tk.Entry(frame, show="*", highlightthickness=1, highlightcolor='black')
        self.new_password_entry.pack()
        tk.Label(frame, text="Initial Deposit:").pack()
        self.initial_balance_entry = tk.Entry(frame, highlightthickness=1, highlightcolor='black')
        self.initial_balance_entry.pack()
        tk.Button(frame, text="Create Account", command=self.create_account).pack(pady=5)
        tk.Button(frame, text="Back", command=lambda: self.show_frame("main")).pack()
        return frame

    def show_frame(self, frame_name):
        if frame_name == "main":
            self.login_frame.pack_forget()
            self.create_account_frame.pack_forget()
            self.account_frame.pack_forget()
            self.button_frame.pack(pady=5)
        elif frame_name == "login":
            self.button_frame.pack_forget()
            self.create_account_frame.pack_forget()
            self.account_frame.pack_forget()
            self.login_frame.pack()
        elif frame_name == "create":
            self.button_frame.pack_forget()
            self.login_frame.pack_forget()
            self.account_frame.pack_forget()
            self.create_account_frame.pack()
        elif frame_name == "account":
            self.button_frame.pack_forget()
            self.login_frame.pack_forget()
            self.create_account_frame.pack_forget()
            self.account_frame.pack()
            self.update_date_label()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if username is '' or password is '':
            messagebox.showwarning("Login Failed", "Username and password cannot be empty.")
            return
        account = self.bank.login(username, password)
        if account is not None:
            self.current_account = account
            messagebox.showinfo("Login Successful", f"Welcome, {account.name}!")
            self.show_frame("account")
        else: #username or password is incorrect
            messagebox.showwarning("Login Failed", "Incorrect username or password")

    def create_account(self):
        username = self.new_username_entry.get().strip()
        password = self.new_password_entry.get().strip()
        
        if username is '' or password is '':
            messagebox.showwarning("Account Creation Failed", "Username and password cannot be empty.")
            return
        try:
            initial_balance = float(self.initial_balance_entry.get())
            # Check if initial balance is negative
            if initial_balance < 0:
                messagebox.showwarning("Account Creation Failed", "Initial balance cannot be negative.")
                return
        except ValueError:
            messagebox.showwarning("Account Creation Failed", "Please enter a valid number for initial balance.")
            return

        if self.bank.create_account(username, password, initial_balance):
            messagebox.showinfo("Account Created", "Account created successfully! Please login.")
            self.reset_ui()
        else: #username already exist
            messagebox.showwarning("Account Creation Failed", "Account creation failed. Username may already exist.")

    def reset_ui(self):
        self.show_frame("main")
        for entry in [self.username_entry, self.password_entry, self.new_username_entry, self.new_password_entry, self.initial_balance_entry]:
            entry.delete(0, tk.END)

    def update_date_label(self):
        self.date_label.config(text=f"Current date: {self.current_date.strftime('%Y-%m-%d')}")

    def update_date(self, days):
        self.current_date += timedelta(days=days)
        self.update_date_label()
        #calculate interest of credit card
        if is_first_day_of_month(self.current_date):
            interest = self.bank.calculate_interest(self.current_account, self.current_date)
            if interest > 0:
                messagebox.showinfo("Interest Calculation", f"Interest charged for unpaid balance last month: ${interest:.2f}")
        #calculate fund change
        if self.current_account.fund_type:
            change = self.bank.fund_change(self.current_account)
            if change > 0:
                messagebox.showinfo("Fund Change", f"Fund balance increased by: ${change:.2f}")
            elif change < 0:
                messagebox.showinfo("Fund Change", f"Fund balance decreased by: ${change:.2f}")

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
        if amount is not None:
            if amount <= 0:
                messagebox.showwarning("Deposit Failed", "Deposit amount must be positive.")
            elif self.bank.deposit(self.current_account, amount):
                messagebox.showinfo("Deposit Result", BankText.DEPOSIT_SUCCESS.format(balance=self.current_account.balance))
            else:
                messagebox.showinfo("Deposit Result", BankText.DEPOSIT_FAILURE)

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
        if amount is not None:
            if amount <= 0:
                messagebox.showwarning("Withdrawal Failed", "Withdrawal amount must be positive.")
            elif self.bank.withdraw(self.current_account, amount):
                messagebox.showinfo("Withdrawal Result", BankText.WITHDRAW_SUCCESS.format(balance=self.current_account.balance))
            else:
                messagebox.showinfo("Withdrawal Result", BankText.WITHDRAW_FAILURE)

    def get_balance(self):
        balance = BankText.BALANCE.format(balance=self.current_account.balance)
        messagebox.showinfo("Account Balance", balance)

    def apply_credit_card(self):
        if not is_first_day_of_month(self.current_date):
            messagebox.showinfo("Application Failed", BankText.NOT_FIRST_DAY)
            return
        elif self.current_account.card_type:
            messagebox.showinfo("Application Failed", "You already have a credit card.")
            return
        else:
            card_types = "\n".join([f"{k}: {v[0]}" for k, v in CARD_INFO.items()])
            card_type = simpledialog.askstring("Apply for Credit Card", f"Choose a credit card type:\n{card_types}")
            if card_type.upper() in CARD_INFO:
                card_type = card_type.upper()
                description = self.bank.get_card_description(card_type)
                if messagebox.askyesno("Confirm Application", f"{description}\n\nConfirm application for this card?"):
                    self.bank.apply_credit_card(self.current_account, card_type)
                    messagebox.showinfo("Application Result", "Application successful!")
            else:
                messagebox.showinfo("Application Result", "Application failed. You may selected an invalid type.")

    def get_credit_card(self):
        if self.current_account.card_type:
            card_info = CARD_INFO[self.current_account.card_type]
            info = BankText.CREDIT_CARD_INFO.format(
                card_name=card_info[0],
                total_credit=self.current_account.total_credit,
                interest_rate=self.current_account.interest_rate * 100,
                available_credit=self.current_account.available_credit,
                unpaid_credit=self.current_account.unpaid_credit,
                points=self.current_account.points
            )
        else:
            info = BankText.NO_CREDIT_CARD
        messagebox.showinfo("Credit Card Information", info)

    def spend(self):
        amount = simpledialog.askfloat("Spend", "Enter spending amount:")
        if amount is not None:
            if amount <= 0:
                messagebox.showwarning("Spending Failed", "Spending amount must be positive.")
                return
            use_credit_card = messagebox.askyesno("Payment Method", "Use credit card?")
            result = self.bank.spend(self.current_account, amount, use_credit_card)
            if result == 'Spending successful with credit card':
                    message = BankText.SPEND_SUCCESS_CREDIT.format(
                        amount=amount,
                        available_credit=self.current_account.available_credit,
                        points_earned=int(amount * self.current_account.points_multiplier),
                        total_points=self.current_account.points
                    )
            elif result == 'Spending successful with balance':
                message = BankText.SPEND_SUCCESS_DEBIT.format(amount=amount, balance=self.current_account.balance)
            else:
                message = result
            messagebox.showinfo("Spending Result", message)

    def make_payment(self):
        if not is_last_day_of_month(self.current_date):
            messagebox.showinfo("Payment Failed", BankText.NOT_LAST_DAY)
            return
        else: 
            if self.current_account.card_type and self.current_account.unpaid_credit > 0: #has card and has unpaid credit
                payment_info = BankText.PAYMENT_INFO.format(
                    unpaid_credit=self.current_account.unpaid_credit,
                    min_payment=max(self.current_account.unpaid_credit * 0.5, 10)
                )
            else: #no card or no unpaid credit
                messagebox.showinfo("Payment Failed", BankText.NO_PAYMENT_NEEDED)
                return

        amount = simpledialog.askfloat("Credit Card Payment", f"{payment_info}\nEnter payment amount:")
        if amount is not None:
            if amount > self.current_account.balance:
                messagebox.showinfo("Payment Failed", "Payment amount exceeds the available balance")
                return
            else:
                result = self.bank.make_payment(self.current_account, amount)
                if result:
                    message = BankText.PAYMENT_SUCCESS.format(amount=amount)
                else:
                    min_payment = max(self.current_account.unpaid_credit * 0.5, 10)
                    if amount < min_payment:
                        message = BankText.PAYMENT_FAILURE_MIN.format(min_payment=min_payment)
                    elif amount > self.current_account.unpaid_credit:
                        message = BankText.PAYMENT_FAILURE_EXCESS.format(unpaid_credit=self.current_account.unpaid_credit)
                    else:
                        message = BankText.PAYMENT_FAILURE_NO_CARD
            messagebox.showinfo("Payment Result", message)

    def redeem_points(self):
        if not self.current_account.card_type:
            messagebox.showinfo("Point Redemption", BankText.NO_CREDIT_CARD_POINTS)
            return
        dialog = RedeemPointsDialog(self.master, REWARDS, self.current_account.points, self.bank.redeem_points)
        self.master.wait_window(dialog)

        if dialog.result is not None:
            choice = dialog.result
            item, points_needed = REWARDS[choice]
            if self.bank.redeem_points(self.current_account, choice):
                message = BankText.REDEEM_SUCCESS.format(item=item, points=self.current_account.points)
                messagebox.showinfo("Redemption Successful", message)
            else:
                message = BankText.REDEEM_FAILURE.format(
                    current_points=self.current_account.points,
                    required_points=points_needed,
                    item=item
                )
                messagebox.showinfo("Redemption Failed", message)
        else:
            messagebox.showinfo("Point Redemption", BankText.REDEEM_CANCELLED)

    def create_fund_account(self):
        if not self.current_account.fund_type:
            fund_types = "\n".join([f"{k}: {v[0]}, {v[1]}" for k, v in FUND_INFO.items()])
            fund_type = simpledialog.askstring("Create Fund Account", f"Choose a fund type:\n{fund_types}").upper()
            if fund_type in FUND_INFO:
                if messagebox.askyesno("Confirm Fund Creation", BankText.FUND_CREATION_CONFIRMATION):
                    self.bank.create_fund_account(self.current_account, fund_type)
                    messagebox.showinfo("Fund Account Creation", "Fund account created successfully!")
            else:
                messagebox.showinfo("Fund Account Creation", "Invalid fund type selected.")
        else:
            messagebox.showinfo("Fund Account Creation", "You already have a fund account.")

    def get_fund_account(self):
        if self.current_account.fund_type:
            fund_info = FUND_INFO[self.current_account.fund_type]
            info = BankText.FUND_ACCOUNT_INFO.format(
                fund_name=fund_info[0],
                fund_balance=self.current_account.fund_balance)
        else:
            info = BankText.NO_FUND_ACCOUNT
        messagebox.showinfo("Fund Account Information", info)

    def invest_fund(self):
        if self.current_account.fund_type:
            amount = simpledialog.askfloat("Invest Fund", "Enter investment amount:")
            if amount is not None and amount <= 0:
                messagebox.showwarning("Investment Failed", "Investment amount must be positive.")
                return
            if self.bank.invest_in_fund(self.current_account, amount):
                messagebox.showinfo("Investment Result", "Investment successful!")
            else:
                messagebox.showinfo("Investment Result", "Investment failed. Your balance is insufficient.")
        else:
            messagebox.showinfo("Investment Result", BankText.NO_FUND_ACCOUNT)

    def withdraw_fund(self):
        if self.current_account.fund_type is not None:
            amount = simpledialog.askfloat("Withdraw Fund", "Enter withdrawal amount:")
            if amount:
                if self.bank.withdraw_from_fund(self.current_account, amount):
                    messagebox.showinfo("Withdrawal Result", "Withdrawal successful!")
                else:
                    messagebox.showinfo("Withdrawal Result", "Withdrawal failed. Your fund balance is insufficient.")
        else:
            messagebox.showinfo("Withdrawal Result", BankText.NO_FUND_ACCOUNT)

    def logout(self):
        self.current_account = None
        self.show_frame("main")

class RedeemPointsDialog(Toplevel):
    def __init__(self, parent, rewards, current_points, redeem_callback):
        super().__init__(parent)
        self.title("Redeem Points")
        self.rewards = rewards
        self.current_points = current_points
        self.redeem_callback = redeem_callback
        self.result = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Current points: {self.current_points}").pack(pady=10)

        self.choice = StringVar()
        for key, (item, points) in self.rewards.items():
            tk.Radiobutton(self, 
                           text=f"{item} ({points} points)", 
                           variable=self.choice, 
                           value=str(key)).pack(anchor='w')

        tk.Button(self, text="Redeem", command=self.redeem).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self, text="Cancel", command=self.cancel).pack(side=tk.RIGHT, padx=10, pady=10)

    def redeem(self):
        choice = self.choice.get()
        if choice:
            self.result = int(choice)
            self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()