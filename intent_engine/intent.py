from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()

# intent definition begins

# WEATHER INTENT
##############################################################
weather_keyword = [
    "weather",
    "forecast",
    "temperature"
]

for wk in weather_keyword:
    engine.register_entity(wk, "weatherKeyword")

engine.register_regex_entity("(?:in|of|at) (?P<location>.*)")

weather_intent = IntentBuilder("weather")\
    .require("weatherKeyword")\
    .require("location")\
    .build()

engine.register_intent_parser(weather_intent)
##############################################################

# TIME INTENT
##############################################################
time_keyword = [
    "time"
]

for tk in time_keyword:
    engine.register_entity(tk, "timeKeyword")

time_intent = IntentBuilder("time") \
    .require("timeKeyword") \
    .build()

engine.register_intent_parser(time_intent)
##############################################################

# SEARCH_SUMMARY INTENT
##############################################################
search_keyword = [
    "search",
    "understand",
    "mean"
]

for sk in search_keyword:
    engine.register_entity(sk, "searchKeyword")

engine.register_regex_entity(".*(?:by|is|a|is a|for) (?P<search_entity>.*)")

search_summary_intent = IntentBuilder("search_summary") \
    .require("searchKeyword")\
    .require("search_entity") \
    .build()

engine.register_intent_parser(search_summary_intent)
##############################################################

# NEWS INTENT
##############################################################
news_keywords = [
    "news",
    "headlines"
]
for nk in news_keywords:
    engine.register_entity(nk, "newsKeywords")

news_cat = [
    'hindi',
    'english'
]

for nc in news_cat:
    engine.register_entity(nc, "newsCategory")

# Define NewsIntent
news_intent = IntentBuilder("news") \
    .require("newsKeywords") \
    .optionally("newsCategory")\
    .build()

# Register the NewsIntent
engine.register_intent_parser(news_intent)
##############################################################

# intent definition ends

def get_intent(command):
    intents = list(engine.determine_intent(command))
    if intents:
        for intent in intents:
            if intent.get('confidence') > 0:
                return intent
    else:
        return {"intent_type" : "null"}