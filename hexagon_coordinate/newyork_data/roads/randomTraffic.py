import geojson
import json
import random

major_jsonfile = open('./major.geojson', 'r+')
major_dict = json.loads(major_jsonfile.read())
minor_jsonfile = open('./minor.geojson', 'r+')
minor_dict = json.loads(minor_jsonfile.read())
giant_dict = {"type": "FeatureCollection", "features": []}
count = 1

for index in range(72):
    road_size = len(major_dict["features"][index]["geometry"]["coordinates"])
    for i in range(road_size - 1):
        new_dict = {"type": "Feature", "properties": {"id": count, "congestion": random.uniform(0.4, 1.2)}}
        coords = [major_dict["features"][index]["geometry"]["coordinates"][i], major_dict["features"][index]["geometry"]["coordinates"][i + 1]]
        new_dict["geometry"] = {"type": "LineString", "coordinates": coords}
        giant_dict["features"].append(new_dict)
        count += 1

for index in range(1370):
    road_size = len(minor_dict["features"][index]["geometry"]["coordinates"])
    for i in range(road_size - 1):
        new_dict = {"type": "Feature", "properties": {"id": count, "congestion": random.uniform(0.2, 1.2)}}
        coords = [minor_dict["features"][index]["geometry"]["coordinates"][i], minor_dict["features"][index]["geometry"]["coordinates"][i + 1]]
        new_dict["geometry"] = {"type": "LineString", "coordinates": coords}
        giant_dict["features"].append(new_dict)
        count += 1

jsonfile = open('./manhattan_traffic_2.geojson', 'w')
r = json.dumps(giant_dict)
jsonfile.write(str(r))
jsonfile.close()