import sys
sys.path.append("/home/aditya/Documents/leah/")
sys.path.append("/home/aditya/Documents/leah/tts_engine")

from skills import weather
from skills import time
from skills import search
from skills import news

# Mapping of intent types to corresponding skill functions
intent_handlers = {
    'weather': weather.get_weather,
    'time' : time.get_time,
    'search_summary' : search.searchSummary,
    'news' : news.playNews
    # Add more intent types and corresponding handlers as needed
}

def process_intent(intent):
    intent_type = intent.get('intent_type')
    if intent_type in intent_handlers:
        # Call the corresponding handler function based on intent_type
        res = intent_handlers[intent_type](intent)
        return res
    else:
        # Default handler for unknown intent types
        print("Unknown intent type")
        return " "
