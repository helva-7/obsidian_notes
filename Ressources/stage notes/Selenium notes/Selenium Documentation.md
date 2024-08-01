- to invokes chrome browser , u need to import the "webdriver" class and write like below : 
```
- from selenium import webdriver

driver = webdriver.Chrome()
```
the chrome browser gonna open and close too quick since there is no instruction , to make it wait for some time , insert "time.sleep(duration)".when the execution ends, the browser automatically closes
- in deep perspectives, the selenium webdriver will not directly invoke browser , between this too , there is something called Chrome Driver service, its a middleman. chrome browser will not give direct permission to any automation tool , each browser has a browser driver 

- the communication goes like this : u talk to Chrome driver and the instruction to automate and perform , the chrome driver interprets all webdriver commands then it triggers the chrome browser. our webdriver
dont talk to the browser directly
![[Pasted image 20240717154623.png]]
- for every chrome version , there is a relevant chrome driver made by the browser vendors ; selenium automatically checks our chrome version

- the driver object we create controls all of chrome browser
- if u want to hit any URL in the browser , use the method : "driver.get("URL")"
- some VPN stricted companies cant let selenium download the driver needed, and doesnt let the selenium the authority to do that , so the user has to search for the driver and its convenient version 
- to maximize the window of the browser we acess , use "**driver.maximize_window**"
- if u want to get the title of the window like the one we set on html , use "**driver.title**" and stock it on a variable 
- to get the URL of the website we are on, maybe after redirecting us to another one , use "**driver.current_url**"
- to hit all these tests on **Firefox**, u simply replace "Chrome()" by "Firefox()" as method of driver object. the same thing with **Edge** browser , u simply replace it with "Edge()"