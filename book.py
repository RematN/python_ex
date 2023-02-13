class Book(object):
    def __init__(self,b_id,b_name,b_price):
        self.b_id = b_id
        self.b_name = b_name
        self.b_price = b_price

    #set
    def set_id(self,b_id):
        self.b_id = b_id
    def set_name(self,b_name):
        self.b_name = b_name
    def set_price(self,b_price):
        self.b_price = b_price
    #get
    def get_id(self):
        return self.b_id 
    def get_name(self):
        return self.b_name
    def get_price(self):
        return self.b_price
    #display
    def __str__(self):
        return '\nbook id:' + str(self.get_id()) + '\nbook name =' + str(self.get_name()) + '\nbook price =' + str(self.get_price())
        
    
books = []
while True:
    choice = input('Enter Choice\n ADD : a \n UPDATE : u \n SEARCH : s \n DELETE : d \n DISPLAY : D \n:')

    match choice:  
        case 'a':
            x = 'y'
            while x == 'y':
                i='i'
                while i =='i':
                    bid = input('Enter book ID :')
                    try:
                        int_test=int(bid)
                        i='p'
                    except Exception as e:
                        print("please enter int value")
                        i='i'
                bname = input('Enter book Name :')
                i='i'
                while i =='i':
                    bprice = input('Enter book Price :')
                    try:
                        int_test=int(bprice)
                        i='p'
                    except Exception as e:
                        print("please enter int value")
                        i='i'
                print()
                books.append(Book(bid,bname,bprice))
                
                x = input('do you want to add another book record? (y/n) :')
        
        case 'u':
                bid =input('Enter Book Id of the record you want to Update:')
                i='i'
                while i =='i':
                    try:
                        int_test=int(bid)
                        i='p'
                        for b in books:
                            if int(b.get_id()) == int(bid) :
                                while True:
                                    x = input('Do you want to update Book Id (y/n):')
                                    if x == 'y':
                                        Id = int(input('Enter new Book Id:'))
                                        b.set_id(Id)
                                        print('Book Id has been updated.\n================== ')
                                        break
                                    else:
                                        break

                                while True:
                                    x = input('Do you want to update Book Name (y/n):')
                                    if x == 'y':
                                        nm = input('Enter new Book Name:')
                                        b.set_name(nm)
                                        print('Book Name has been updated.\n================== ')
                                        break
                                    else:
                                        break
                                while True:
                                    x = input('Do you want to update Book Price (y/n):')
                                    if x == 'y':
                                        i='i'
                                        while i =='i':
                                            pr = input('Enter new Book Price:')
                                            try:
                                                int_test=int(pr)
                                                i='p'
                                                b.set_price(pr)
                                                print('Book Price has been updated.\n================== ')
                                                break
                                                
                                            except Exception as e:
                                                print("please enter int value")
                                                i='i'
                                    else:
                                        break
                        else:
                            print('Record Not Found.\n=====================')    
                    except Exception as e:
                        print("please enter digit only")
                        i='i'
            
        case 's':
                i='i'
                while i =='i':
                    bid = input('Enter Book Id you want to Search:')
                    try:
                        int_test=int(bid)
                        i='p'
                        for b in books:
                           if int(b.get_id()) == int(bid):
                             print('Book id:' + str(b.get_id()) + '\nBook Name:' + b.get_name() + '\nBook Price:' + str(b.get_price()))
                             break
                        else:
                            print('Record Not Found.\n====================')
                            
                    except Exception as e:
                        print("please enter digits only")
                        i='i'
            
        case 'd':
                i='i'
                while i =='i':
                    bid = input('Enter Book id you want to delete:')
                    try:
                        int_test=int(bid)
                        i='p'
                        for b in books:
                            if int(b.get_id()) == int(bid) :
                         # if b.get_id() == bid:
                                books.remove(b)
                                print('Record Deleted.\n=====================')
                                break
                        else:
                            print('Record Not Found.\n====================')
                            
                    except Exception as e:
                        print("please enter int value")
                        i='i'

        case 'D':
            print('========== Book Details ==========')
            if books == []:
                print('opps! Records Not Found.')
            for b in books:

                print('Book Id:',b.get_id())
                print('Book Name:',b.get_name())
                print('Book Price:',b.get_price())
            print("=============================")
        case _:
            print('Wrong Choice.')
            break