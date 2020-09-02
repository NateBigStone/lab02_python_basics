from dataclasses import dataclass

"""
Type in the dataclass code from the slides/video
Add one more field: gpa, a float
Write a main function to create some example Student objects with some example names, college_id and GPA values.
Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included.
Add some comments in your code to compare the dataclass version to the "traditional" version
"""

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

#Using a dataclass vs the tradition version uses much less code and simplifies this common usage of classes

def main():

    alice = Student('Alice', 12345, 2.0)
    bob = Student('Bob', 98765, 3.6)
    nate = Student('Nate', 8675309, 4.0)

    print(alice)
    print(bob)
    print(f'Name: {nate.name} GPA: {nate.gpa}')


if __name__ == "__main__":
    main()
