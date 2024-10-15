import googlemaps
from datetime import datetime

# Step 3.1: Initialize the client with your API key
gmaps = googlemaps.Client(key='AIzaSyCu4cPgsCXjhg9Ez_HHKudv37VKdOt20WU')  # Replace with your actual API key

# Step 3.2: Geocoding an address
def geocode_address(address):
    result = gmaps.geocode(address)
    if result:
        location = result[0]['geometry']['location']
        print(f"Coordinates of {address}: Latitude: {location['lat']}, Longitude: {location['lng']}")
        return location
    else:
        print(f"Could not geocode address: {address}")

# Step 3.3: Get distance between two places
def get_distance(origins, destination):
    result = gmaps.distance_matrix(origins, destination)
    if result:
        distance = result['rows'][0]['elements'][0]['distance']['text']
        duration = result['rows'][0]['elements'][0]['duration']['text']
        print(f"Distance from {origins} to {destination}: {distance}, Travel time: {duration}")
    else:
        print(f"Couldn't calculate distance from {origins} to {destination}")

# Step 3.4: Find nearby places (e.g., restaurants)
def find_nearby_places(location, place_type="restaurant"):
    places = gmaps.places_nearby(location=location, radius=1500, type=place_type)
    if places:
        print(f"Top {place_type.capitalize()}s near this location:")
        for place in places['results'][:5]:  # Displaying only top 5 results
            print(f"- {place['name']} with rating {place.get('rating', 'N/A')}")
    else:
        print(f"No places of type {place_type} found near this location")

# Step 3.5: Get directions from one place to another
def get_directions(start, end):
    directions = gmaps.directions(start, end, mode="driving", departure_time=datetime.now())
    if directions:
        print(f"Directions from {start} to {end}:")
        for step in directions[0]['legs'][0]['steps']:
            print(step['html_instructions'])  # Instructions in HTML format
    else:
        print(f"Couldn't get directions from {start} to {end}")

# Step 4: Execute the functions with example data
if __name__ == "__main__":
    # Replace with actual addresses/locations
    vnit_address = "Visvesvaraya National Institute of Technology, Nagpur"
    
    # Step 4.1: Get geocode for VNIT
    vnit_location = geocode_address(vnit_address)

    if vnit_location:
        # Step 4.2: Get distance from VNIT to Nagpur Railway Station
        get_distance(vnit_address, "Nagpur Railway Station")

        # Step 4.3: Find nearby restaurants
        find_nearby_places(vnit_location, place_type="restaurant")

        # Step 4.4: Get directions from VNIT to Nagpur Airport
        get_directions(vnit_address, "Nagpur Airport")
