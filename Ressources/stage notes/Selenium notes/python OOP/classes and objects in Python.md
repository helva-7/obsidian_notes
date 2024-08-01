- classes are user defined blueprint or prototype with all the operators which we can use their functionalities by utilizing the classes
- these functionalities are methods, instance variables, constructor ...etc
# Constructor and its role in OOP 
- if u dont define the constructor on a class , a default constructor will be assigned to it 
- to declare a constructor in python , we use __ init __ ()
- dont forget about the difference between class variable and instance variables (u dont have to declare instance variables inside the class) or declare it like this 
```
	variable = None # public variables 
	_variable = None # protected variables
	__variable = None # private variables
```
- always use the "self" keyword in creating and calling variable names inside the class 
- to create an object , just call the class name with attributes with no "new" keyword 

# Inheritance concepts
 - to create a child class that will inherit from Parent class , we simply write 
 
```
class ChildClass(ParentClass):
```
- working on multiple files , we need to import classes from them to the one we working on
