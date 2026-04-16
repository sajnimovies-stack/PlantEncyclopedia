‎
+61
-50
Lines changed: 61 additions & 50 deletions


Original file line number	Diff line number	Diff line change
@@ -1,71 +1,82 @@
[Plant.id](https://web.plant.id) offers [plant identification](https://web.plant.id/plant-identification-api/) and [plant diseases identification](https://web.plant.id/plant-health-assessment/) API based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/), you can use these client's code available in this repository to speed-up the development of your implementation.
[Plant.id](https://web.plant.id) by [kindwise](https://kindwise.com) offers [plant identification](https://web.plant.id/plant-identification-api/)
and [plant health assessment](https://web.plant.id/plant-health-assessment/) API based on machine learning. 
Once you [register and obtain the API key](https://admin.kindwise.com/signup), you can use these client's code available in this repository to speed-up the development of your implementation.

# Plant.id API v2
# Plant.id API v3

See our **[documentation](https://github.com/flowerchecker/Plant-id-API/wiki)** for the full reference.
Don't know how to code? Try the [online demo](https://plant.id/). 🌐
 - **[documentation](https://plant.id/docs)** - full API reference
 - **[python SDK](https://github.com/flowerchecker/kindwise-api-client)** - simply use API from pyhon
 - documentation on **[Postman](https://www.postman.com/winter-shadow-932363/workspace/kindwise/collection/24599534-c4a4048d-ed97-4532-8980-3159ddbfe629)**
 - try [online demo](https://plant.id/)
 - more [python examples](python)

## Plant Identification 🌱

Send us your plant images encoded in base64, and get a list of possible species suggestions with additional information.
Send us your plant images, and get a list of possible species suggestions with additional information.
```bash
pip install kindwise-api-client
```
```python
from kindwise import PlantApi
api = PlantApi('your_api_key')
identification = api.identify('../images/unknown_plant.jpg', details=['url', 'common_names'])
print('is plant' if identification.result.is_plant.binary else 'is not plant')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()
```
Same example in pure python

```python
import base64
import requests

# encode images to base64
with open("unknown_plant.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]
with open('../images/unknown_plant.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    "https://api.plant.id/v2/identify",
    json={
        "images": images,
        "modifiers": ["similar_images"],
        "plant_details": ["common_names", "url"],
    },
    headers={
        "Content-Type": "application/json",
        "Api-Key": "-- ask for one: https://web.plant.id/api-access-request/ --",
    }).json()
for suggestion in response["suggestions"]:
    print(suggestion["plant_name"])    # Taraxacum officinale
    print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
    print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale
    'https://api.plant.id/v3/identification',
    params={'details': 'url,common_names'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)
identification = response.json()
print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])
    print(f'probability {suggestion["probability"]:.2%}')
    print(suggestion['details']['url'], suggestion['details']['common_names'])
    print()
```

Response example: [response_species_identification.json](https://github.com/flowerchecker/Plant-id-API/blob/master/response_species_identification.json).

## Health Assessment 🥀

Send us your ill plant photos encoded in base64, and get a list of possible health issues your plant suffers from.
Send us your ill plant images, and get a list of possible health issues your plant suffers from.

```Python
import base64
import requests
# encode images to base64
with open("ill_plant.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]
response = requests.post(
    "https://api.plant.id/v2/health_assessment",
    json={
        "images": images,
        "modifiers": ["similar_images"],
        "disease_details": ["description", "treatment"],
    },
    headers={
        "Content-Type": "application/json",
        "Api-Key": "-- ask for one: https://web.plant.id/api-access-request/ --",
    }).json()
if not response["health_assessment"]["is_healthy"]:
    for suggestion in response["health_assessment"]["diseases"]:
        print(suggestion["name"])   # water deficiency
        print(suggestion["disease_details"]["description"])    # Water deficiency is...
from kindwise import PlantApi

api = PlantApi('your_api_key')
identification = api.health_assessment('../images/unhealthy_plant.jpg', details=['description', 'treatment'])

print('is healthy' if identification.result.is_healthy.binary else 'has disease')
for suggestion in identification.result.disease.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['description'])
    print(suggestion.details['treatment'])
    print()
```

Response example: [response_health_assessment.json](https://github.com/flowerchecker/Plant-id-API/blob/master/response_health_assessment.json).
