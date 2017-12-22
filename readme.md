# Python-Cafe-Finder

A python script that takes a user location input and retrieves a list of local coffee shops using the Google Places API. 


### Process
> 1: User enters the desired location. EX: "Santa Monica"

> 2: The script takes the user's input and concatenates it into the HTTP request GET parameter.

> 3: The request is made to the Google Places API. The script then parses through the JSON response and makes a list of "place" objects. 

> 4: The list of cafes are iterated through and their contents printed to the console. 

##
### Example Request
```sh
https://maps.googleapis.com/maps/api/place/textsearch/json?query=Cafe+coffee+near+Santa+Monica&key=KEY&sensor=false
```
