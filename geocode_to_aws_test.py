import urllib

API_KEY = "AIzaSyBvB3pY50QDVBdwxq5C768gFATYOduI0Q4"
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='
fields = 'formatted_address'
def get_response(url, geostring, fields, key):
    url = "{0}{1}&inputtype=textquery&fields={2}&key={3}".format(url, geostring, fields, key)
    response = urllib.request.urlopen(url)
    print(response)

def get_geostring():
    geostring = input("Where are you at?")
    geostring = geostring.replace(" ", "%20")
    return geostring
    # TODO: send to AWS

get_response(url, get_geostring(), fields, API_KEY)
