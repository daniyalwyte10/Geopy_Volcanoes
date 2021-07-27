import folium
import pandas

data = pandas.read_csv("4.1 Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_select(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


Map = folium.Map(location=[43.655323, -79.401981], zoom_start=10, titles='Mapbox bright')
fg = folium.FeatureGroup(name='My Map')

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,  popup=str(el) + " m",fill_color=color_select(el),color='grey', fill_opacity=0.7,fill=True ))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='cp1252').read()))
Map.add_child(fg)
Map.save("Map1.html")
