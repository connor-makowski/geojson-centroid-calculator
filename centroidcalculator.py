import json

def Read_JSON (filename):
    with open (filename) as infile:
        output = json.load(infile)
    return output

def Write_JSON (filename, object):
    with open( filename, 'w') as outfile:
        json.dump(object, outfile)

def Calc_Centroid (coordinates, multiPolygon):
    max_lat=-180
    max_lon=-180
    min_lat=180
    min_lon=180
    for l1 in coordinates:
        for l2 in l1:
            if multiPolygon:
                for l3 in l2:
                    max_lat=max(l3[0], max_lat)
                    min_lat=min(l3[0], min_lat)
                    max_lon=max(l3[1], max_lon)
                    min_lon=min(l3[1], min_lon)
            else:
                max_lat=max(l2[0], max_lat)
                min_lat=min(l2[0], min_lat)
                max_lon=max(l2[1], max_lon)
                min_lon=min(l2[1], min_lon)
    return [(max_lat+min_lat)/2 , (max_lon+min_lon)/2]

def Calc_All_Centroids (geojsonObject, propertiesId):
    features=geojsonObject['features']
    centroids={}
    for feature in features:
        id=feature['properties'][propertiesId]
        if feature['geometry'] != None:
            coordinates=feature['geometry']['coordinates']
            multiPolygon= True if feature['geometry']['type']=='MultiPolygon' else False
            centroid=Calc_Centroid(coordinates, multiPolygon)
            centroids[id]=centroid
    return centroids

def Centroid_Calculator (infile, outfile, propertiesId):
    geojsonObject=Read_JSON(infile)
    centroids=Calc_All_Centroids(geojsonObject, propertiesId)
    Write_JSON(outfile, centroids)
