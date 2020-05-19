from savingsaccount import SavingsAccount
class RestrictedSavingsAccount(SavingsAccount):
    MAX_WITHDRAWALS = 3        
    def __init__(self, name, pin, balance = 0.0):
        SavingsAccount.__init__(self, name, pin, balance)
        self.counter = 0
    def withdraw(self, amount):
        if self.counter == \
           RestrictedSavingsAccount.MAX_WITHDRAWALS:
            return "Withdrawls maxed out for month"
        else:
            message = SavingsAccount.withdraw(self, amount)
            if message == None:
                self.counter += 1
            return message
    def resetCounter(self):
        self.counter = 0
