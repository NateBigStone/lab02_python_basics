"""
Start with the program from part 1.
In this version, an author can't publish two books with the same name.
When the publish function is called, print an error message if the book given has the same name as a book currently in
the books list.
"""

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print(f'You have already entered "{title}"!')
        else:
            self.books.append(title)

    def __str__(self):
        titles = '", "'.join(self.books) or "No published books"
        return f'''{self.name}, Books: "{titles}"'''


def main():

    #Test Authors
    a1 = Author("Dr. Seuss")
    a1.publish('Wacky Wednesday')
    a1.publish('The Tooth Book')
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
    a3.publish('Homegoing')
    print(a3)

    a4 = Author("Nate G")
    print(a4)

if __name__ == "__main__":
    main()
