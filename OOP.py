class Book:
    #attributes - size, pages, colour, thickness
    #methods - turning a page, closing, opening

    def __init__(self, title, author, pages, current_page) : #spec_page , last_page, alternative_page):
        #assignment to object attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1  #assign by default
        #self.spec_page = 
    
    def bookmark_page(self):
        self.bookmark = self.current_page
    
    def turn_page(self):
        self.current_page += 1

   # def turn_spec_page(self):
   #     self.spec_page = 

    def bookmark_page_alternate(self, alternative_page):
        self.bookmark= alternative_page

    def go_back_to_start(self):
        if self.current_page == self.pages -1:
            self.current_page = 1
        else:
            self.current_page -= 1



    #def last_page(self):
       # self.last_page =

    def bookmark_page(self, page_to_set):
        if self.current_page != page_to_set:
            self.bookmark = self.current_page

    #string representation
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"
    
    def __len__(self):
        return self.pages

    #create a method turn back the page
    

my_book = Book("A great book", "me", 198, 1)
# print(my_book.__str__())
print(my_book)
print(my_book.bookmark) #attr
my_book.turn_page() #method
my_book.bookmark_page(page_to_set= 120) 
print(my_book.bookmark)
my_book.bookmark_page_alternate(100)

#jpage = input("What page would you like to jump to?")
#turnto = my_book.turn_page(jpage) 
#print(turnto)
