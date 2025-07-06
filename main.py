from fastapi import FastAPI, Request
import httpx
import traceback
import random
import html
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Environment keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
QUOTE_API_KEY = os.getenv("QUOTE_API_KEY")

FAREWELLS = [
    "Goodbye! Have a great day 😊",
    "See you later! Stay awesome!",
    "Farewell – keep shining!"
]

@app.post("/webhook")
async def webhook(req: Request):
    try:
        body = await req.json()
        intent = body["queryResult"]["intent"]["displayName"]
        parameters = body["queryResult"].get("parameters", {})

        async with httpx.AsyncClient() as client:
            if intent == "custom.smalltalk.time":
                try:
                    res = await client.get(
                        "https://api.api-ninjas.com/v1/worldtime?city=delhi",
                        headers={"X-Api-Key": QUOTE_API_KEY}
                    )
                    res.raise_for_status()
                    data = res.json()
                    time_str = data.get("datetime", "")
                    return {"fulfillmentText": f"🕒 Current time in Delhi: {time_str}"}
                except Exception:
                    return {"fulfillmentText": "Sorry, I couldn't fetch the time right now."}

            elif intent == "custom.smalltalk.quote":
                try:
                    res = await client.get(
                        "https://api.api-ninjas.com/v1/quotes",
                        headers={"X-Api-Key": QUOTE_API_KEY}
                    )
                    res.raise_for_status()
                    q = res.json()[0]
                    return {"fulfillmentText": f"\u201c{q['quote']}\u201d \u2014 {q['author']}"}
                except Exception:
                    return {"fulfillmentText": "Sorry, I couldn't fetch a quote at the moment."}

            elif intent == "custom.smalltalk.ask_advice":
                try:
                    res = await client.get("https://api.adviceslip.com/advice")
                    res.raise_for_status()
                    advice = res.json()["slip"]["advice"]
                    return {"fulfillmentText": f"💡 Here's a tip: {advice}"}
                except Exception:
                    return {"fulfillmentText": "Couldn't fetch advice right now."}

            elif intent == "custom.smalltalk.compliment_user":
                try:
                    res = await client.get("https://complimentr.com/api")
                    res.raise_for_status()
                    compliment = res.json()["compliment"].capitalize()
                    return {"fulfillmentText": f"💬 {compliment}"}
                except Exception:
                    return {"fulfillmentText": "You're awesome, even if I can't fetch a compliment!"}

            elif intent == "custom.smalltalk.hobby_suggestion":
                try:
                    res = await client.get(
                        "https://api.api-ninjas.com/v1/hobbies?category=general",
                        headers={"X-Api-Key": QUOTE_API_KEY}
                    )
                    res.raise_for_status()
                    hobbies = res.json()
                    if isinstance(hobbies, list) and hobbies:
                        hobby = hobbies[0].get("hobby", "reading")
                    else:
                        hobby = "painting or writing"
                    return {"fulfillmentText": f"🎯 Try this hobby: {hobby}"}
                except Exception:
                    return {"fulfillmentText": "Try something fun like painting or gardening!"}

            elif intent == "custom.smalltalk.weather":
                city = parameters.get("geo-city", "Delhi")
                try:
                    res = await client.get(
                        f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
                    )
                    data = res.json()
                    if "error" in data:
                        return {"fulfillmentText": "Couldn't find the weather for that city."}
                    temp = data["current"]["temp_c"]
                    feels = data["current"]["feelslike_c"]
                    condition = data["current"]["condition"]["text"]
                    return {"fulfillmentText": f"🌤️ The weather in {city} is {condition} with {temp}°C. Feels like {feels}°C."}
                except Exception:
                    return {"fulfillmentText": "Unable to get weather data."}

            elif intent == "custom.smalltalk.joke":
                try:
                    res = await client.get("https://v2.jokeapi.dev/joke/Any?format=txt&type=single")
                    return {"fulfillmentText": res.text.strip()}
                except Exception:
                    return {"fulfillmentText": "Couldn't fetch a joke right now."}

            elif intent == "custom.smalltalk.fun_fact":
                try:
                    res = await client.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
                    fact = res.json().get("text", "Here's a fun fact for you!")
                    return {"fulfillmentText": f"🧠 Did you know? {fact}"}
                except Exception:
                    return {"fulfillmentText": "Couldn't fetch a fun fact."}

            elif intent == "custom.smalltalk.quiz":
                try:
                    res = await client.get("https://opentdb.com/api.php?amount=1&type=multiple")
                    data = res.json()["results"][0]
                    question = html.unescape(data["question"])
                    correct = html.unescape(data["correct_answer"])
                    incorrect = [html.unescape(ans) for ans in data["incorrect_answers"]]
                    options = incorrect + [correct]
                    random.shuffle(options)
                    option_text = "\n".join([f"- {opt}" for opt in options])
                    return {"fulfillmentText": f"❓ {question}\n{option_text}\n\n(Answer: {correct})"}
                except Exception:
                    return {"fulfillmentText": "Couldn't load a quiz right now."}

            elif intent == "custom.smalltalk.travel":
                try:
                    country = parameters.get("geo-country", "India")
                    res = await client.get(f"https://restcountries.com/v3.1/name/{country}")
                    info = res.json()[0]
                    capital = info.get("capital", ["Unknown"])[0]
                    pop = info.get("population", 0)
                    return {"fulfillmentText": f"🌍 The capital of {country} is {capital} and its population is {pop:,}."}
                except Exception:
                    return {"fulfillmentText": "Couldn't fetch travel data right now."}

            elif intent == "custom.smalltalk.farewell":
                return {"fulfillmentText": random.choice(FAREWELLS)}

        return {"fulfillmentText": "❗ I couldn't match that intent."}

    except Exception:
        traceback.print_exc()
        return {"fulfillmentText": "⚠️ An error occurred. Please try again later."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
