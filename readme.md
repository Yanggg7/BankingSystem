# Bank Account Management System - Developer Documentation

## Project Overview

This project is a bank account management system based on Python and Tkinter. It provides basic bank account operations, credit card management, and investment functions. The system uses a graphical user interface (GUI) to provide a user-friendly interaction experience.

## Project Structure

The project consists of the following main files:

1. main.py
2. bank_gui.py
3. bank.py
4. account.py
5. config.py
6. Text.py
7. utils.py

## File Details

### 1. main.py

The main program entry, responsible for launching the GUI application.

Main functions:
- Create Tkinter root window
- Instantiate BankGUI class
- Start the main event loop

### 2. bank_gui.py

Defines the BankGUI class, responsible for creating and managing the graphical user interface.

Main classes and methods:
- `BankGUI` class:
  - `__init__`: Initialize GUI
  - `init_ui`: Create main interface
  - `Main_Menu`: Create main menu
  - `create_login_frame`: Create login frame
  - `create_account_frame`: Create account creation frame
  - `show_frame`: Switch between different frames
  - `login`: Handle login logic
  - `create_account`: Handle account creation logic
  - `deposit`, `withdraw`, `get_balance`: Basic account operations
  - `apply_credit_card`, `get_credit_card`, `make_payment`, `redeem_points`: Credit card related operations
  - `create_fund_account`, `get_fund_account`, `invest_fund`, `withdraw_fund`: Investment related operations
  - `update_date`: Update system date

### 3. bank.py

Defines the Bank class, responsible for handling core business logic.

Main class and methods:
- `Bank` class:
  - `create_account`: Create new account
  - `login`: User login
  - `deposit`, `withdraw`: Deposit and withdrawal operations
  - `apply_credit_card`: Apply for credit card
  - `spend`: Handle spending
  - `calculate_interest`: Calculate credit card interest
  - `make_payment`: Handle credit card payment
  - `redeem_points`: Redeem points
  - `create_fund_account`, `fund_change`, `invest_in_fund`, `withdraw_from_fund`: Fund related operations

### 4. account.py

Defines Account and CreditCard classes, representing user accounts and credit cards.

Main classes:
- `Account` class: Basic account information
- `CreditCard` class (inherits from Account): Additionally includes credit card and investment related attributes, all operations are based on the CreditCard class.

### 5. config.py

Stores system configuration information.

Main contents:
- GUI settings (title, size, font)
- Initial date
- Frame titles
- Button configurations
- Reward information
- Credit card information
- Fund information

### 6. Text.py

Defines the BankText class, storing text information used in the system, preventing the GUI file from becoming too bulky.

Main contents:
- Success/failure messages for various operations
- Prompts related to credit cards and funds

### 7. utils.py

This document contains auxiliary functions.

Main functions:
- `is_first_day_of_month`: Determine if it's the first day of the month
- `is_last_day_of_month`: Determine if it's the last day of the month


