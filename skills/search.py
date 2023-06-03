import requests
import json

def searchSummary(query):
    url = "https://duckduckgo-duckduckgo-zero-click-info.p.rapidapi.com/"

    querystring = {
        "q": query['search_entity'],
        "format": "json",
        "skip_disambig": "1",
        "no_redirect": "1",
        "no_html": "1",
        "callback": "process_duckduckgo"
    }

    headers = {
        "X-RapidAPI-Key": "fb6c842de3msh06df12f2cc6bc9fp1b969bjsn7c5e3959f58e",
        "X-RapidAPI-Host": "duckduckgo-duckduckgo-zero-click-info.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jsonp_response = response.content.decode("utf-8").replace("process_duckduckgo(", "")[:-2]
    data = json.loads(jsonp_response)

    if "Abstract" in data:
        abstract = data["Abstract"]
        first_sentence = abstract.split(".")[0] + "."
        return first_sentence
    else:
        return "Sorry, I could not understand that."