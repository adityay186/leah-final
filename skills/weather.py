import requests

def get_weather(city):
    params = {
      'access_key': '4fc85ccf51de68cc4bd43405d678cd4a',
      'query': city["location"]
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    res = "In " + str(api_response['location']['name']) + ',' \
    + str(api_response['location']['region']) + " its " \
    + str(api_response['current']['temperature']) \
    + " degrees" \
    + " and " + str(api_response["current"]["weather_descriptions"][0])
    
    return res