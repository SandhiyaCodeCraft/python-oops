from item import Item
item1 = Item("xty",700,1)
item1.sendEmail()
item1.__connect()#we cant access/see it outside the class,because it is private in the class.
Abstraction;Abstraction is the concept of hiding the internal implementation and showing/acess only the necessary details to the user.
here the only necessary method sendEmail()is shown /exposed to user and others are hidden by making it private.
