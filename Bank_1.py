import smtplib

class BankAccount:

    def __init__(self,user_name,ac_no,ph_no,i_amount,email_id):
        self.user_name = user_name
        self.ac_no = ac_no
        self.ph_no = ph_no
        self.i_amount = i_amount
        self.email_id = email_id

    def credit(self,amt,ac_n):
        self.amt = amt
        self.ac_n = ac_n
        if self.amt>=0:
            self.i_amount = self.i_amount + self.amt
            print(self,i_amount)
            return ("Credited Amount: " + self.amt + "Current Amount: " + self.i_amount)
        else:
            print('please enter credit amount grater than 0')
        
    def debit(self,amt,ac_n):
        self.amt = amt
        self.ac_n = ac_n
        if (self.i_amount >= self.amt):
            self.i_amount = self.i_amount - self.amt
            print(self.i_amount)
            send_mail(("Debited Amount: " + self.amt + "Current Amount: " + self.i_amount),self.email_id)
            # return ("Debited Amount: "+ self.amt+"Current Amount:"+ self.i_amount)
            if (self.i_amount <= 500 and self.i_amount >= 0):
                if (self.i_amount == 0):
                    print("Oops! Your current balance is zero.")
                else:
                    print('You have reached to minimum balance.')
            elif (self.i_amount == amt):
                print("Oops! Your current balance is zero.") 
        else:
            print("Insufficient Balance")
        
def display(self):
    # print("Current Balance: ", self.i_amount)
    return ("Current Balance: ", self.i_amount)
# def transfer(self,amt,ac_no):
    #     self.ac_no = ac_no
    #     self.amt = amt        
def send_mail(message,email_id):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # s = smtplib.SMTP_SSL(host='localhost', port=80)
    s.starttls()
    s.login('rehmatnoyda@gmail.com','iyrclfvigmbgrbxp')

    s.sendmail("rehmatnoyda@gmail.com",email_id ,message)
    s.quit()

def usr_choice():
    ac_no = int(input("Enter your account number: "))
    return ac_no
    
print("STARTING BANK SOFTWARE.....")
ask_usr = int(input("How many account do you have: "))

account_obj_list = []
for n in range (0,ask_usr):
    print("enter account information for user no: " + str(n+1))
    user_name = input("User Name: ")
    ac_no = int(input("Account No.: "))
    ph_no = int(input("Phone no.: "))
    i_amount = float(input("Initial amount: "))
    email_id = input("Enter your mail id :")
    if i_amount >=0:
        obj = BankAccount(user_name,ac_no,ph_no,i_amount,email_id)
        account_obj_list.append(obj)
    else:
       print('please enter initial amount greater than 0') 
print("STARTING CLIENT EXPERIENCE.....")

while True: 

    choice = input("What do you want to do? : credit = c /debit = d /check_balance = cb /transfer = t: ")
    if (choice == "c"):
        x = usr_choice()
        for i in account_obj_list:
            
            if i.ac_no==x:
                amt = float (input("Amount: "))
                send_mail(i.credit(amt,x),i.email_id)
                i.display()
            else:
                print('')

    elif(choice == "d"):
        x = usr_choice()
        for i in account_obj_list:
            
            if i.ac_no==x:
                amt = float (input("Amount: "))
                i.debit(amt,x)
                send_mail(i.debit(amt,x),i.email_id)
                i.display()
            else:
                print('')
        
    elif(choice == "cb"):
        x = usr_choice()
        for i in account_obj_list:
            
            if i.ac_no==x:
                send_mail(i.display(),i.email_id)
                i.display()
            else:
                print('')

    elif(choice == "t"):
        acc1 = int(input("Enter acc no. from which you want to transfer: "))
        acc2 = int(input("Enter acc no. to which you want to transfer: "))
        amt = float (input("Amount: "))

        do_not_credit=False
        for i in account_obj_list:
            if i.ac_no==acc1:
                if amt > i.i_amount:
                    do_not_credit=True
                else:
                    i.debit(amt,acc1)
                    send_mail(i.debit(amt,acc1),i.email_id)
                    # i.display()
            else:
                print('')

        if do_not_credit!=True:
            for i in account_obj_list:
                if i.ac_no==acc2:
                    # i.credit(amt,acc2)
                    send_mail(i.credit(amt,acc2),i.email_id)
                    # i.display()
            else:
                print('')
        else:
            print("Insufficient Balasnce")

    else:
        print("OOPS!! WRONG CHOICE")
        break