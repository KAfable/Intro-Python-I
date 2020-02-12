# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


location = LatLon(50, 100)
print(location.lat)
print(location.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.


class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"


wp1 = Waypoint(25, 30, "Land's End")
print(wp1.lat)
print(wp1.lon)
print(wp1.name)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"{self.name}, diff {self.difficulty}, size {self.size} {self.lat}, {self.lon}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)

# Print it--also make this print more nicely
print(geocache)

# ? why is it called dunder?
# ? is there a way to have geocache inherit and build on the __self__ or do I have to overwrite it?
# ? should I be using dictionaries to actually input or to make the actual inputs easier?
