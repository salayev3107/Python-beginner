
class book():
     def __init__(self, title, author,pages):
         self.title = title
         self.author = author
         self.pages = pages
     def print_info(self):
         #print('инфо о книге: ',self.title, self.author,self.pages)
         print(f'инфо о книге: {self.title}, автор--{self.author} , страниц--{self.pages}' )
     def is_long(self):
         return self.pages > 300

book1 = book('Molxona',  'джорж Оруел',  500)
book1.print_info()
book1.is_long()
print(book1.is_long())        
