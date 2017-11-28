import urllib.request
import json


def return_get(location_name):
    return "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Cafe+coffee+near+" \
          + location_name + "&key=AIzaSyC_KZyErDtZ42CuFscO2l5YseWaV8MCHrQ&sensor=false"


def places_api_request(request_url):
    web_data = urllib.request.urlopen(request_url)
    data = web_data.read()
    encoding = web_data.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))


def display_cafes():



def main():
    location_name = input("Enter Location Name: ")
    request_url = return_get(location_name)
    json_data = places_api_request(request_url)

    for cafe in json_data["results"]:
        print(cafe["name"])

main()
