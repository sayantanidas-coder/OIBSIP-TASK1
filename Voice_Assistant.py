import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import smtplib
import requests
import time
import threading

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to voices[1].id for female voice
engine.setProperty('rate', 200)

# Speak text aloud
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Listen to microphone and convert speech to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is down.")
        return ""
    return query.lower()

# Tell the current time and date
def tell_day_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d %B %Y")
    speak(f"The time is {time_str} and today's date is {date_str}")

# Fetch weather using OpenWeatherMap API
def get_weather(city="Kolkata"):
    api_key = "1d02a7a89e59d9e2cc07561047009011"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response['main']['temp']
        desc = response['weather'][0]['description']
        speak(f"The temperature in {city} is {temp}°C with {desc}")
    else:
        speak("Sorry, I couldn't fetch the weather information.")

# Search and summarize from Wikipedia
def get_wikipedia_answer(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")

# Send email via SMTP
def send_email(to, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("sayantanidas20jul@gmail.com", "152021@Fam")  # App password if 2FA enabled
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail("sayantanidas20jul@gmail.com", to, email)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak("Failed to send the email.")
        print(e)

# Reminder functionality
reminders = []

def add_reminder(task, time_str):
    reminders.append((task, time_str))
    speak(f"Reminder set for '{task}' at {time_str}")

def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for task, t in reminders:
            if t == now:
                speak(f"Reminder: {task}")
        time.sleep(60)

# Start reminder thread
threading.Thread(target=check_reminders, daemon=True).start()

# Identify intent from query
def intent_match(query):
    query = query.lower()
    if "time" in query or "date" in query:
        return "datetime"
    elif "email" in query or "send mail" in query:
        return "send_email"
    elif "weather" in query or "temperature" in query:
        return "weather"
    elif "who is" in query or "what is" in query or "tell me about" in query:
        return "wiki"
    elif "remind me" in query or "set reminder" in query:
        return "reminder"
    elif "search" in query:
        return "search"
    elif "open youtube" in query:
        return "youtube"
    elif "exit" in query or "bye" in query:
        return "exit"
    else:
        return "unknown"

# Main assistant loop
if __name__ == "__main__":
    speak("Hello! I am your Voice friend. With what can I help you?")
    while True:
        query = take_command()
        if not query:
            continue

        intent = intent_match(query)

        if intent == "datetime":
            tell_day_time()
        elif intent == "weather":
            speak("Which city's weather should I check?")
            city = take_command()
            get_weather(city)
        elif intent == "wiki":
            get_wikipedia_answer(query)
        elif intent == "send_email":
            speak("Who is the recipient?")
            to = take_command().replace(" ", "") + "@gmail.com"
            speak("What is the subject?")
            subject = take_command()
            speak("What should I say?")
            message = take_command()
            send_email(to, subject, message)
        elif intent == "reminder":
            speak("What should I remind you about?")
            task = take_command()
            speak("At what time? Please say it like 15:30.")
            time_str = take_command()
            add_reminder(task, time_str)
        elif intent == "search":
            speak("What should I search for?")
            topic = take_command()
            webbrowser.open(f"https://www.google.com/search?q={topic}")
            speak(f"Here are the search results for {topic}")
        elif intent == "youtube":
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif intent == "exit":
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I didn't understand that. Try again.")
