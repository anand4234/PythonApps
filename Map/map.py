import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
lt = data["LAT"]
ln = data['LON']
elv = data['ELEV']
map = folium.Map(location=[38.5, -99.09], tiles="Stamen Toner", zoom_start=6)
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


def set_color(ele):
    if ele > 2000:
        return "red"
    elif ele < 1000:
        return "green"
    else:
        return "orange"


for lt, ln, ele in zip(lt, ln, elv):
    fgv.add_child((folium.CircleMarker(location=[lt, ln], popup="Elevation:%s" % ele, fill_color=set_color(ele),
                                       fill_opacity=0.7, color="grey")))

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
