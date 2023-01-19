# lab at https://www.linkedin.com/learning/intermediate-python-for-non-programmers/classes-and-weather?autoSkip=true&autoplay=true&resume=false&u=75768826

# this virtual environment created with
# python -m venv weather_venv
# source weather_venv/bin/activate (Unix) OR .\weather_venv\Scripts\activate (Windows)
# deactivate


import requests


class City:
    def __init__(self, name, lat, lon, units='metric'):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            # paste in url with variable names placed in api parameters
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=3df07b70b0411e8f64ea4ea4a3ae297a")

        except:
            print("Something went wrong - no internet?")

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")


# include Wellington lon and lat - check order
my_city = City("Wellington", 41.2924, 174.7787)
my_city.temp_print()
