from item import Item
item1 = Item("xty",700,1)
item1.sendEmail()

Abstraction;Abstraction is the concept of hiding the internal implementation and showing only the necessary details to the user.
here we can abstract  we cant see the process how the mail sent.i.e the other functions called in sendEmail()beacuse that is private we cant access or see it outside the class.i hide it by making it private inside the class
