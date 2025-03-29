import config
from weather import Weather
from geopy import distance
from country_facts import Facts


class Airport:

    def __init__(self, ident, active=False, data=None):
        self.ident = ident
        self.active = active

        if data is None:
            sql = "SELECT ident, name, latitude_deg, longitude_deg, iso_country FROM airport WHERE ident = %s"
            cur = config.conn.cursor()
            cur.execute(sql, (ident,))
            res = cur.fetchall()
            if len(res) == 1:
                self.ident = res[0][0]
                self.name = res[0][1]
                self.latitude = float(res[0][2])
                self.longitude = float(res[0][3])
                self.iso_country = res[0][4]
        else:
            self.name = data['name']
            self.latitude = float(data['latitude'])
            self.longitude = float(data['longitude'])

    def find_nearby_airports(self):
        nearby_list = []

        lat_min = self.latitude - config.max_lat_dist
        lat_max = self.latitude + config.max_lat_dist
        lon_min = self.longitude - config.max_lon_dist
        lon_max = self.longitude + config.max_lon_dist

        sql = """
            SELECT ident, name, latitude_deg, longitude_deg 
            FROM airport 
            WHERE latitude_deg BETWEEN %s AND %s 
            AND longitude_deg BETWEEN %s AND %s
        """
        cur = config.conn.cursor()
        cur.execute(sql, (lat_min, lat_max, lon_min, lon_max))
        res = cur.fetchall()

        for r in res:
            if r[0] != self.ident:
                data = {'name': r[1], 'latitude': r[2], 'longitude': r[3]}
                nearby_apt = Airport(r[0], False, data)
                nearby_apt.distance = self.distanceTo(nearby_apt)
                if nearby_apt.distance <= config.max_distance:
                    nearby_list.append(nearby_apt)
                    nearby_apt.co2_consumption = self.co2_consumption(nearby_apt.distance)
        return nearby_list


    def fetchWeather(self, game):
        self.weather = Weather(self, game)
        return

    def fetchData(self, game):
        self.country_data = Facts(self, game)
        return

    def distanceTo(self, target):

        coords_1 = (self.latitude, self.longitude)
        coords_2 = (target.latitude, target.longitude)
        dist = distance.distance(coords_1, coords_2).km
        return int(dist)

    def co2_consumption(self, km):
        consumption = config.co2_per_flight + km * config.co2_per_km
        return consumption




