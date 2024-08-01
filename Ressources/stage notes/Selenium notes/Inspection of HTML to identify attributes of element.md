- working with a practice page , we gonna learn how to fill some fields on the page using selenium .
1. first , we gonna get the url of the page we are practicing on by the "driver.get("URL")" method 
2. there is many ways to identify the elements , and by entering the content only on the field we desire to fill and thats is by using **Locators** which are : ID , **Xpath**, **CSS SELECTOR** ,**Classname** , name , **Linktext**
3. to get them , we should inspect our page . after knowing the type of our element and its name , we use the function below 
```
 driver.find_element(By.Name , "name").send_keys("value needed to be filled")
 
# in this ex we are using the name element . make sure to import the "By"
```
4. we fill the selected fields by the ".send_keys("value as a string")" like the example above 
5. for the checkbox , we us the ".click()" method 
6. if needed , u can create any path of the element on the page desired to select , its called **Xpath**
7.  to create an Xpath ,syntax => 
```
	XPATH => //tagname[@attribute='value']
```
tagname is the type of element , attribut is the attribut of the html tag

- now we gonna see the **CSS selector**, the syntax is 
```
	CSS SELECTOR => tagname[attribute='value'] 
	#idvalue => this is for pointing on a tag by its id
	.classname => this is for pointing on a tag by its classname
```
- there is a function that check if the output given is the one we desire to get , its called **assert**. per example , i want to check if the word "Success" is there on the output printed,
```
assert "success" in message 
```
if its there , the program will run , if not , the program will fail

- now we gonna see the **linktext** method of  locators :
- there is two ways to locate with linktext , there is By.LINK_TEXT which locates the exact visible text given , and By.PARTIAL_LINK_TEXT which only locates an element by a partial match of the text given, these locators only work if that text is wrapped by a link and has an "a" tag
- we can locate text also with Xpath like this per example :"//button[text()='TEXTWANTED']"

in generating a Xpath or a css selector and wants to go from parent tag to children tags , u add a "/" , just like a directory

# Dropdown 
- if we encounter a static dropdown , meaning a "select" tag . we use the **Select** class , import it and use it like in the code file "locators" 

# dynamic text fetching
- to get the dynamic text inside a text field , the ".text" method wont work since its not statically put on the website .
- what we can use is "**.get_attribute("value")**". the "value" is a javascript DOM element ; which means there is an attribute named value that save get the value given each time we enter the website  