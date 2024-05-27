

class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
         
    def __add__(self, other):
        return  Location((self.lat + other.lat) / 2,( self.lon + other.lon )/ 2)
    
    def __eq__(self, other):
        return self.lat == 3456 and self.lon == 9594
    
latitude = Location(1234, 7866)
longitude = Location(5678, 3454)
result = latitude+longitude
print(" Latitude:", result.lat)
print(" Longitude:", result.lon)

if result == Location(3456, 9594):
    print("reached location")
else:
    print("wrong location")


