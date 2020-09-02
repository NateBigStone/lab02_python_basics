"""
Create a new class called Author
An Author has a name, and a list of books published
When you create a new Author, they don't have any books. So create an empty books list attribute in __init__
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles
Write a main function to test your class, create some example authors, and publish some example books

"""

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self,title):
        self.books.append(title)

    def __str__(self):
        titles = '", "'.join(self.books) or "No published books"
        return f'''{self.name}, Books: "{titles}"'''


def main():

    #Test Authors
    a1 = Author("Dr. Seuss")
    a1.publish('Wacky Wednesday')
    a1.publish('The Tooth Book')
    a1.publish('What Was I Scared Of?')
    a1.publish('Oh, the Places You\'ll Go!')
    print(a1)

    a2 = Author("Neil Gaiman")
    a2.publish('Coraline')
    a2.publish('Norse Mythology')
    a2.publish('The Sleeper and the Spindle')
    print(a2)

    a3 = Author("Yaa Gyasi")
    a3.publish('Transcendent Kingdom')
    a3.publish('Homegoing')
    print(a3)

if __name__ == "__main__":
    main()
