class net_bank(object):
    def __init__(self):
        self.initial_amount = 0
        
        
    def credit(self, amount):
        self.amount = amount
        self.initial_amount += amount
        print("Credited Amount: ", self.amount)

    def debit(self, amount):
        self.amount = amount
        if (self.initial_amount >= self.amount):
            self.initial_amount -= amount
            print("Debited Amount: ", self.amount)
            if (self.initial_amount <= 500 and self.initial_amount >= 0):
                if (self.initial_amount == 0):
                    print("Oops! Your current balance is zero.")
                else:
                    print('You have reached to minimum balance.')
            elif (self.initial_amount == amount):
                print("Oops! Your current balance is zero.") 
               
        else:
            print("Insufficient Balance")
    
    def get_bal(self):
        print("Current Balance :", self.initial_amount)
    

ob = net_bank()
while True:

    c = input('enter choice credit(c) / debit(d) / status(s):')

    if c == 'c':
        c_bal = int(input("Enter the amount you want to credit:"))   
        ob.credit(c_bal)
        
        #x.credit()
    elif c == 'd':
        d_bal = int(input("Enter the amount you want to debit:"))
        ob.debit(d_bal)

    elif c == 's':
        ob.get_bal()
    else:
        break
    

        



