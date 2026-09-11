# 🎙️ Python Voice Assistant

A beginner-friendly **Python Voice Assistant** that listens to voice commands through a microphone, understands the user's speech, performs basic actions, and responds using text-to-speech.

This project was created to practice **Speech Recognition, Text-to-Speech, Functions, Exception Handling, Date & Time, and Web Browser Automation in Python.**

## ✨ Features

* 🎤 Capture voice input using `SpeechRecognition`
* 👋 Respond to greetings such as "Hello" and "Hi"
* 🕐 Tell the current time
* 📅 Tell the current date
* 🌐 Perform Google searches using voice commands
* 🔊 Respond to the user using `pyttsx3`
* ❌ Handle speech recognition errors gracefully
* 🚪 Exit the assistant using commands such as "Goodbye" or "Exit"

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition**
* **PyAudio**
* **pyttsx3**
* **datetime**
* **webbrowser**

## 📁 Project Structure

```text
Voice-Assistant/
│
├── voice_assistant.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-assistant.git
```

### 2. Open the project folder

```bash
cd voice-assistant
```

### 3. Install the required libraries

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

Or install them using the requirements file:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```bash
python voice_assistant.py
```

The assistant will start and ask you to speak.

Make sure your **microphone is connected and working**.

## 🗣️ Available Voice Commands

| Voice Command                | Action                                |
| ---------------------------- | ------------------------------------- |
| `Hello`                      | Responds with a greeting              |
| `Hi`                         | Responds with a greeting              |
| `What is the time?`          | Tells the current time                |
| `What is the date?`          | Tells the current date                |
| `Search for Python`          | Opens Google and searches for Python  |
| `Search for pandas tutorial` | Searches Google for a pandas tutorial |
| `Goodbye`                    | Stops the assistant                   |
| `Exit`                       | Stops the assistant                   |
| `Stop`                       | Stops the assistant                   |

## 🔄 How It Works

The assistant follows this basic workflow:

```text
🎤 Microphone
      ↓
Speech Recognition
      ↓
Convert Speech → Text
      ↓
Process User Command
      ↓
Perform Requested Action
      ↓
Text-to-Speech
      ↓
🔊 Voice Response
```

## 🧩 Main Python Concepts Practiced

This project helps practice several important Python concepts:

* Functions
* `if`, `elif`, and `else`
* `while` loops
* Exception handling
* Importing modules
* Working with dates and times
* String manipulation
* User input
* Web browser automation
* Third-party Python libraries

## ⚠️ Error Handling

The assistant handles situations where:

* The microphone does not detect speech
* Speech cannot be understood
* The speech recognition service is unavailable
* The user gives an unknown command

For example:

```text
Assistant: Sorry, I could not understand you. Please repeat.
```

## 🚀 Future Improvements

More features can be added to make the assistant more powerful:

* 🌦️ Weather information
* 📺 Open YouTube
* 🎵 Play music
* 📖 Wikipedia search
* 🧮 Voice calculator
* 💻 Open applications
* 📰 News updates
* 🔋 Check battery status
* 📂 Open files and folders
* 🤖 AI-powered responses
* 🔐 Voice-based authentication
* 🗣️ More natural conversations

## 🎯 Learning Goal

The main goal of this project is to understand how Python can interact with **microphone input, speech recognition, text-to-speech, web browsers, and external libraries** to create a simple voice-controlled application.

## 👨‍💻 Author

**Saeed**

Python Developer | Computer Science Student

---

⭐ If you found this project useful, consider giving the repository a star!
