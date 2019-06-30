import folium
import pandas

data = pandas.read_json("comedylocation.json")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])

map = folium.Map(location=[40.750567, -73.993539], zoom_start=12)#National Christmas Tree

fg = folium.FeatureGroup(name="Comedy Clubs")

for lt, ln, names in zip(lat,lon,name):
	fg.add_child(folium.Marker(location = [lt, ln], popup = names, icon = folium.Icon(color='red')))

fgl = folium.FeatureGroup(name="Population")

fgl.add_child(folium.GeoJson(data=open('world.json','r',
encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']
 < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Map1.html")
