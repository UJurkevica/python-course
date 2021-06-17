import requests

base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
nasa_image = requests.get(base_url)

nasa_data = nasa_image.json()

print(nasa_data['url'])


