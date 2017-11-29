from place import Place
import urllib.request
import json


def get_search():
    location_name = input("Enter Location Name: ")
    region_name = input("Enter Region Name: ")
    search = location_name + " " + region_name
    return search.replace(" ", "+")


def return_get(location_name):
    return "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Cafe+coffee+near+" \
          + location_name.replace(" ", "+") + "&key=AIzaSyC_KZyErDtZ42CuFscO2l5YseWaV8MCHrQ&sensor=false"


def places_api_request(request_url):
    web_data = urllib.request.urlopen(request_url)
    data = web_data.read()
    encoding = web_data.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))


def init_places_list(json_data):
    places = []

    if len(json_data["results"]) > 0:
        for cafe_data in json_data["results"]:
            places.append(Place(cafe_data))

    return places


def display_cafes(places_list):
    if len(places_list) > 0:
        for cafe in places_list:
            cafe.print_place_information()
    else:
        print("No places found")


def main():
    location = get_search()
    request_url = return_get(location)
    json_data = places_api_request(request_url)

    places_list = init_places_list(json_data)

    display_cafes(places_list)


main()
