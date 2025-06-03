from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type 

class Account:
    def __init__(self, name):
        self.name = name
        self._balance = 0  
        self.frozen = False
        self.loan = 0
        self.transactions = []  
        self.min_balance = 500
        self.deposits = []

    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self._balance += amount
            transaction = Transaction(f"You deposited: {amount}", amount, "Deposit")
            self.transactions.append(transaction)
            return f"Confirmed, new balance is {self.get_balance()}."
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount > 0 and self._balance - amount >= self.min_balance:
            self._balance -= amount
            transaction = Transaction(f"You have withdrawn: {amount}", amount, "Withdrawal")
            self.transactions.append(transaction)
            return f"Your new balance is {self.get_balance()}."
        if amount > self._balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."

    def transfer_funds(self, amount, other_account):
        if amount <= 0:
            return "You can only transfer a positive amount."
        if self._balance - amount < self.min_balance:
            return "Insufficient funds for transfer."
        self._balance -= amount
        other_account.deposit(amount)  
        transaction = Transaction(f"Transferred {amount} to {other_account.name}", amount, "Transfer")
        self.transactions.append(transaction)
        return f"New balance is {self.get_balance()}."

    def get_balance(self):
        return self._balance  


    def calculate_loan_limit(self):
        total_deposits = sum(self.deposits) 
        loan_limit = total_deposits//2
        return loan_limit


    def get_loan(self, amount):
        if amount < 0:
            return "Input a positive amount"
        if amount <= self.calculate_loan_limit() : 
            self.loan += amount
            self._balance += amount
            transaction = Transaction(f"Loan requested: {amount}", amount, "Loan")
            self.transactions.append(transaction)
            return f"You requested a loan of {amount}."
        else:
            return "Check your loan limit"

    def pay_loan(self, amount):
        if amount > 0:
            if amount <= self.loan:
                self.loan -= amount
                self._balance -= amount
                transaction = Transaction(f"Loan repaid: {amount}", amount, "Loan Repayment")
                self.transactions.append(transaction)
                return f"You repaid {amount} and your new loan is {self.loan}."
            else:
                excess_payment = amount - self.loan
                self._balance -= self.loan  
                self._balance += excess_payment  
                transaction = Transaction(f"Loan repaid: {self.loan} (excess payment: {excess_payment})", self.loan, "Loan Repayment")
                self.transactions.append(transaction)
                return f"You repaid your loan of {self.loan}. Excess payment of {excess_payment} has been deposited back to your account."
        return "Repayment amount must be positive."

    def account_details(self):
        return f"{self.name}, your balance is {self.get_balance()} and your loan is {self.loan}."

    def transfer_ownership(self, new_name):
        self.name = new_name
        return f"Changed ownership to {self.name}."

    def statement(self):
        for trans in self.transactions:
            return "\n".join([f"{trans.date_time}: {trans.narration} - {trans.amount} ({trans.transaction_type})"])

    def interest(self):
        interest = self._balance * 0.05
        self._balance += interest
        transaction = Transaction(f"Interest applied: {interest}", interest, "Interest")
        self.transactions.append(transaction)
        return f"Your interest was {interest} and your new balance is {self.get_balance()}."

    def freeze(self):
        self.frozen = True
        return "Account has been frozen for security reasons."

    def unfreeze(self):
        self.frozen = False
        return "Account has been unfrozen."

    def close_account(self):
        self._balance = 0
        self.loan = 0  
        self.transactions.clear()
        self.min_balance = 0
        return "Account closed."
























