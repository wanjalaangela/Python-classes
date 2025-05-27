class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.frozen = False
        self.loan = 0
        self.transactions =[]
        self.min_balance = 500
        self.new_account = []
        
    
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self.balance += amount
            self.transactions.append(f" You deposited:{amount}")
            return f"Confirmed,new balance is {self.balance}."


            # WITHDRAW

    def withdraw(self, amount):
        if amount > 0 and self.balance-amount >self.min_balance:
            self.withdrawals.append(amount)
            self.balance -= amount
            self.transactions.append(f"You have withdrawn {amount}")
            return f"your new balance is {self.balance}"

        if amount > self.balance:
            return "Insufficient funds."

    #  TRANSFER FUNDS

    def transfer_funds(self, amount):
        if amount <=0:
            return "You can only transfer positive amount"
        self.new_account.append(amount)
        self.balance -= amount
        self.transaction.append(f"Transferred {amount} to {self.new_account}")
        return f"New balance is {self.balance}"

    #  GET BALANCE

    def get_balance(self):
        return f" Dear {self.name} your current balance is {self.balance}"

    #   LOANS

    def get_loan(self, amount):
        if amount>0:
            self.loan += amount
        return f"You requested a loan of {amount}"

    #   PAY LOAN

    def pay_loan(self, amount):
        if amount > 0 :
            self.loan -= amount
            self.balance -= amount
            return f"You repaid {amount} and your new loan is {self.loan}"


    #    DETAILS 

    def account_details(self):
        return f"{self.name},your balance is {self.balance}and your loan is {self.loan}"

        # OWNERSHIP

    def transfer_ownership (self, new_name):
        self.name = new_name
        return f"Changed ownership to {self.name}"

    #  STATEMENT

    def statement (self):
        for i in self.transaction:
            return f"Your transaction is {self.transaction}"

    # INTEREST

    def interest (self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transaction.append(f"Interest applied to amount is {interest}")
        return f"Your interest was {interest}and your new balance is {self.balance}"


        # Freeze

    def freez(self):
        self.frozen = True
        return f"Account has been frozen for security reason"

        # UNFREEZ

    def un_freeze(self):
        self.frozen = False
        return f"Account has been unfrozen"

        # CLOSE ACCOUNT

    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan.clear()
        self.transaction.clear()
        self.min_balance = 0