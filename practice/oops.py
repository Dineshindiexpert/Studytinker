class smartlib:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        
    def printbook(self):
        print(f"The book name is {self.name} and author is {self.author}")
        
class library(smartlib):
    
    def __init__(self, name, author, publish_year):
        super().__init__(name, author) 
        self.publish_year = publish_year

    def premiumbook(self):
        print(f"The book '{self.name}' was published in {self.publish_year}")

# 1. smartlib ka object
book1 = smartlib("Ramayan", "Valmiki")
book1.printbook()

# 2. library (Child class) ka object
premium_book = library("Bhagavad Gita", "Vyasa", 1999)
premium_book.premiumbook()
