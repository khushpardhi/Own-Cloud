#!/usr/bin/env python3
import cgi
import geocoder

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("    <title>Geolocation and Google Maps</title>")
print("</head>")
print("<body>")
print("    <h1>My Location</h1>")

try:
    # Get the user's geolocation using the 'geocoder' library
    location = geocoder.ip('me')
    
    if location.ok:
        latitude = location.latlng[0]
        longitude = location.latlng[1]
        
        # Display coordinates
        print(f"    <p>Your current coordinates: {latitude}, {longitude}</p>")
        
        # Generate Google Maps link
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f'    <a href="{google_maps_url}" target="_blank">Open in Google Maps</a>')
    else:
        print("    <p>Location information is unavailable.</p>")
except ImportError:
    print("    <p>Python 'geocoder' library is required for geolocation.</p>")
except Exception as e:
    print(f"    <p>Error: {str(e)}</p>")

print("</body>")
print("</html>")
