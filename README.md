# Voice Assistant (TASK-1)

## Objective

The primary objective of this project is to design and implement a speech-driven virtual assistant capable of performing a range of useful tasks through natural voice interaction. The assistant should be able to listen to spoken commands, understand the user's intent, respond via speech, and execute specific functions like checking the weather, sending emails, opening websites, retrieving information from Wikipedia, and setting timely reminders. This project aims to simulate a basic real-world AI assistant and enhance user interaction through automation and voice-based computing.

## Description

This project presents a Python-based voice assistant that interacts with users through voice commands, processes them in real-time, and responds with appropriate actions or spoken feedback. The assistant makes use of key Python libraries and external APIs to function effectively:

- **`speech_recognition`** is used for converting user voice input into text.
- **`pyttsx3`** enables text-to-speech conversion for vocal responses.
- **`datetime`**, **`webbrowser`**, and **`threading`** are used for performing background tasks like showing the current time, opening web pages, and scheduling reminders.
- **OpenWeatherMap API** is used to fetch real-time weather information.
- **Wikipedia API** provides brief answers for general knowledge queries.
- **SMTP protocol** is used for composing and sending emails securely.

The assistant includes a built-in intent recognition system to identify commands like "what is the time", "send email", "remind me", etc., and route the request to the correct function. A background thread continuously checks for due reminders and notifies the user when the time arrives. The assistant also gracefully handles errors like unrecognized speech or connectivity issues.

This modular and scalable design makes the assistant a strong prototype for larger projects involving AI, natural language processing (NLP), or automation.

## Features

- **Voice Recognition**: Converts speech input into text using Google’s Speech Recognition API.
- **Text-to-Speech Output**: Converts textual replies into speech for vocal interaction.
- **Current Date and Time**: Announces current system time and date on request.
- **Weather Updates**: Provides live temperature and weather conditions using a city name.
- **Wikipedia Search**: Fetches and reads a summary of any topic from Wikipedia.
- **Email Sending**: Sends emails by collecting recipient, subject, and message via voice commands.
- **Reminder System**: Sets and monitors user-defined reminders and notifies at the specified time.
- **Google Search**: Opens a browser to search any topic online.
- **YouTube Launching**: Opens YouTube through the default browser.
- **Intent Detection**: Identifies and processes user intent from voice input keywords.

## Conclusion

This Voice Assistant project is a comprehensive demonstration of how voice-controlled applications can enhance user interaction and system accessibility. It combines multiple technologies—speech processing, API integration, task automation, and threading—to deliver a functional virtual assistant. This prototype not only simplifies everyday tasks but also showcases how conversational interfaces are becoming a core component of modern user experiences. With further development, this assistant can be expanded to support advanced NLP, machine learning-driven decision making, offline capabilities, and integration with smart devices, making it suitable for real-world applications in smart homes, personal productivity tools, or accessibility software.
