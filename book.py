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
        return 'book id =' + str(self.get_id()) + 'book name =' + str(self.get_name()) + 'book price =' + str(self.get_price())
        
  
  
    
books = []
choice = input('Enter Choice\n ADD : a \n UPDATE : u \n SEARCH : s \n DELETE : d \n DISPLAY : D \n')

match choice:  
    case 'a':
        x = 'y'
        while x == 'y':
            bid = int(input('Enter book ID :'))
            bname = input('Enter book Name :')
            bprice = int(input('Enter book Price :'))
            print()
            book = Book(bid,bname,bprice)
            books.append(book)
            x = input('do you want to add another book record? (y/n) :')
    
    case 'u':
    case 's':
    case 'd':
    case 'D':
        for b in books:
            print('Book Id:',b.get_id())
            print('Book Name:',b.get_name())
            print('Book Price:',b.get_price())
            print()
    case _:
        




else:
    print('Wrong Choice.')