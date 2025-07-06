
# 🤖 AI Small Talk Chatbot (Dialogflow ES + FastAPI + Public APIs)

A production-grade **Conversational AI chatbot** that uses **Dialogflow ES**, **FastAPI**, and **live public APIs** to deliver human-like interactions including jokes, weather, quotes, trivia, time, compliments, and more.

> Built to impress top-tier engineering teams at **Google**, **Microsoft**, **Amazon**, and **Meta** — this project combines NLU, scalable APIs, and clean webhook architecture.

---

## 🌟 Features

| Intent                            | API / Source                                 | Description                                         |
|----------------------------------|----------------------------------------------|-----------------------------------------------------|
| `custom.smalltalk.weather`       | `weatherapi.com`                             | Get real-time weather for any city                 |
| `custom.smalltalk.time`          | `api.api-ninjas.com/worldtime`               | Accurate local time by city                        |
| `custom.smalltalk.quote`         | `api.api-ninjas.com/quotes`                  | Fetch motivational quotes                          |
| `custom.smalltalk.joke`          | `jokeapi.dev`                                | Return one-liner jokes                             |
| `custom.smalltalk.fun_fact`      | `uselessfacts.jsph.pl`                       | Share fun, random facts                            |
| `custom.smalltalk.ask_advice`    | `adviceslip.com`                             | Provide random life advice                         |
| `custom.smalltalk.compliment_user`| `complimentr.com`                            | Deliver genuine compliments                        |
| `custom.smalltalk.hobby_suggestion`| `api.api-ninjas.com/hobbies`                | Suggest random hobbies                             |
| `custom.smalltalk.quiz`          | `opentdb.com`                                | Trivia-based multiple-choice quiz                  |
| `custom.smalltalk.travel`        | `restcountries.com`                          | Capital & population of any country                |
| `custom.smalltalk.farewell`      | Internal logic                               | Randomized goodbye messages                        |

---

## ⚙️ Tech Stack

- **Dialogflow ES** – Natural Language Understanding & Intent Management  
- **FastAPI** – High-performance async Python backend  
- **httpx** – Async HTTP client for fast API calls  
- **ngrok** – Local tunnel for webhook testing  
- **dotenv** – Secure API key management via environment variables  

---

## 📁 Project Structure

```bash
smalltalk-chatbot/
├── main.py              # FastAPI webhook logic
├── requirements.txt     # Dependencies
├── .env                 # API keys (not committed)
├── ngrok.exe            # For local tunnel (Windows)
├── __pycache__/         # Python bytecode cache
└── README.md            # You're reading it
```

---

## 🔐 .env File

Create a `.env` file in the root directory:

```env
WEATHER_API_KEY=your_weatherapi_key_here
QUOTE_API_KEY=your_api_ninjas_key_here
```

You can get free API keys from:

- https://weatherapi.com  
- https://api-ninjas.com  

---

## 🚀 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI server

```bash
uvicorn main:app --reload --port 8000
```

### 3. Start ngrok in a second terminal

```bash
ngrok http 8000
```

### 4. Paste your `ngrok` HTTPS URL in Dialogflow's Fulfillment Webhook

Example:

```bash
https://a1b2c3d4.ngrok-free.app/webhook
```

---

## 🧠 Dialogflow Integration

1. Go to [Dialogflow ES Console](https://dialogflow.cloud.google.com/)
2. Create a new agent → `SmallTalkBot`
3. Enable **Webhook Fulfillment**
4. Create custom intents:
   - `custom.smalltalk.weather`
   - `custom.smalltalk.joke`
   - `custom.smalltalk.time`
   - ... (same as in the Features table above)
5. In each intent, enable **Use webhook** for fulfillment

---

## 💬 Example Conversations

| User Input                 | Bot Response Example                                                   |
|---------------------------|------------------------------------------------------------------------|
| “Tell me a joke”          | "Why don’t scientists trust atoms? Because they make up everything!"  |
| “What’s the weather?”     | "🌤️ The weather in Mumbai is Sunny with 32°C. Feels like 35°C."       |
| “Give me advice”          | "💡 Here's a tip: Always trust your instincts."                        |
| “Suggest a hobby”         | "🎯 Try this hobby: Calligraphy"                                       |
| “What’s the time in London?” | "🕒 Current time in London: 17:45:22"                             |

---

## ✅ Why This Project Stands Out

- 🔁 End-to-End Flow: User intent → NLP → Webhook → Real API → Fulfilled Response  
- ⚡ Asynchronous Architecture: FastAPI + httpx for blazing-fast performance  
- 🔒 Secure & Scalable: Clean .env + modular codebase  
- 🧠 NLU-Driven: Intent-based interaction model with custom contexts  
- 🧪 Test-Ready: Works locally with ngrok; ready to deploy on Cloud Run  
- 🧰 Job-Worthy: Strong signal for ML, AI, and cloud interviews at top tech companies  

---

## 🧠 Built For

- AI Engineer interviews  
- Google/Microsoft/Meta projects  
- Live chatbot demos  
- Portfolio/resume GitHub showcase  
- Hackathons, product prototypes  

---

## 🌍 Future Scope

- 🔌 Add voice support (Dialogflow Phone Gateway or Twilio)  
- 📱 Connect to Telegram, WhatsApp, or a web frontend  
- ☁️ Deploy to Google Cloud Run or AWS Lambda  
- 💬 Add context-based memory (session storage)  
- 🔐 OAuth-based personalization  

---

## 📮 Contact

> Created with ❤️ by [@Sahil-567](https://github.com/Sahil-567)  
> For questions or collaboration, DM me on GitHub or LinkedIn.

---

> "The best way to predict the future is to build it." — Alan Kay
