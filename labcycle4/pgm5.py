class Publisher:
    def __init__(self,name) -> None:
        self.name=name
class Book(Publisher):
    def __init__(self, name,title,author) -> None:
        super().__init__(name)
        self.title=title
        self.auth=author
    def display(self):
        print("Title:{} \nAuthor:{}".format(self.title,self.auth))

class Python(Book):
    def __init__(self, name, title, author,price, pages) -> None:
        super().__init__(name, title, author)
        self.price=price
        self.pg=pages
    def display(self):
        super().display()
        print("Price:${} \nNo of Pages:{}".format(self.price,self.pg))

py = Python('mcc','Advanced python','Balaguruswamy',90,345)
py.display()