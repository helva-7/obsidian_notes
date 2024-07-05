- a reverse proxy is a server that sit as the middleman between the internet and the web servers ,it intercepts the requests from clients and talks to the web server on behalf of the clients contrary to the forward proxy that sit between the clients and the internet  
- reasons to use the reverse proxy server is to :
	1. it could be used to protect a website since the ip address of the websites are hidden behind the proxy 
	2. its used for load balancing since one website handling millions of users every day is unlikely to be able to handle the traffic with a single server ,by balancing between incoming requests for mutliple websites by a single reverse proxy server 
	3. a reverse proxy caches static content : a piece of content could be cached on the server for a period of time 
	4. handles the ssl encryption protocol 