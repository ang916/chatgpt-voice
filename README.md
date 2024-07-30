# Simple Virtual Assistant

This project is a simple virtual assistant using Python, Tkinter for GUI, Whisper for speech recognition, OpenAI's GPT-3.5-turbo for generating responses, and Google Cloud Text-to-Speech for converting text responses to speech. The assistant listens to user's voice input, processes it, and provides a spoken response.

## Table of Contents
- [Download](#download)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Download
You can download the example mic image here: 

![Download the Image](/mic1.png)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ang916/chatgpt-voice.git

2. **Install the Required Dependencies**: Install the required Dependencies in the requirements.txt

3. **API KEY**: Make sure you have your own **OpenAI API key** and **GOOGLE CLOUD CREDENTIAL KEY**.

4. **Hide API Key**: (Windows)
   ```bash
   setx OPENAI_API_KEY "your_openai_api_key"

## Usage

1. **Run the file**:
   ```bash
   python3 chatgpt_voice_assistant.py
   
2. **Interact with the Assistant**:
-   Click the mic button to start speaking.
-   The assistant will recognize your speech, process it, and provide a response both in text and speech.

##  Features
-   Voice Recognition: Utilizes Whisper for recognizing spoken input.
-   Conversational AI: Integrates OpenAI's GPT-3.5-turbo for generating responses.
-   Text-to-Speech: Uses Google Cloud Text-to-Speech to convert text responses to speech.
-   Graphical User Interface: Built with Tkinter, featuring a mic button and text output areas.
