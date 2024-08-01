- to read or write any file using python u must do 2 things : 
		1. u must open the file and assign it to a variable ```
		if the text file is not on the same path as the py file , u must insert the whole location of the file
```
file = open('test.txt')  
```
2. u must close it "file.close()" to prevent data leaks
3. use with open('file','r') or 'w' to read and write without using the file.close everytime
# Error handling 
- to make an exception , u should write 
```
if condition not met :
	raise Exception("message desired to display")
```
- we can make the code break when a condition is not met by using
	"assert(condition that should be true)"
- try catch mechanism : we use "try catch" when we write a block of code and we are thinking it gonna make an error so we write that code inside of the "try" section .then , it will stop and then it will go in the "catch" section , we write the code that we should execute when that error accurs 
- in python , we dont use the keyword "catch" , we use **"except"** and next to it "as"