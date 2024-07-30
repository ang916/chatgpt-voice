# import libraries
import tkinter as tk
from whisper_mic.whisper_mic import WhisperMic
import threading
from openai import OpenAI
from google.cloud import texttospeech
import os
import pygame
import uuid  # for generating unique filenames

client = OpenAI()

# Set up authentication for Google Cloud Text-to-Speech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Ang/Desktop/fyp1/credential_key.json"

# Initialize Pygame for playing audio
pygame.mixer.init()

# Create and set up Google Cloud Text-to-Speech client
tts_client = texttospeech.TextToSpeechClient()

# Query setup
conversation_history = [{"role": "system", "content": "You are a helpful assistant. Your name is GPT."}]

# Define a separate thread for the button click action to prevent GUI freeze
def mic_button_clicked():
   # Create a thread to handle the time-consuming operation
   thread = threading.Thread(target=handle_button_click)
   thread.start()

# Define the main operation of mic button
def handle_button_click():
   # Create whisper mic instance
   mic = WhisperMic(model="base", english=True)

   text_output1.delete("1.0", tk.END)  # Clear previous content
   text_output2.delete("1.0", tk.END)

   text_output1.insert(tk.END, "Start speaking...")
   mic_input = mic.listen(timeout=7)

   text_output1.delete("1.0", tk.END)  # Clear previous content
   text_output1.insert(tk.END, "Recognized input: " + mic_input)
   conversation_history.append({"role": "user", "content": mic_input})

   # Get response from ChatGPT
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=conversation_history)

   text_output2.insert(tk.END, "GPT: " + response.choices[0].message.content)

   # Convert text response to speech using Google Cloud Text-to-Speech
   tts_response = response.choices[0].message.content
   synthesize_speech(tts_response)

# Function to synthesize speech using Google Cloud Text-to-Speech
def synthesize_speech(text):
   input_text = texttospeech.SynthesisInput(text=text)

   # Select the language and gender of the voice
   voice = texttospeech.VoiceSelectionParams(
       language_code="en-US",
       ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

   # Select the type of audio file you want returned
   audio_config = texttospeech.AudioConfig(
       audio_encoding=texttospeech.AudioEncoding.MP3)

   # Perform the text-to-speech request
   response = tts_client.synthesize_speech(
       input=input_text, voice=voice, audio_config=audio_config)

   # Generate a unique filename
   filename = f"output_{uuid.uuid4().hex}.mp3"

   # Save the audio file
   with open(filename, "wb") as out:
       out.write(response.audio_content)

   # Ensure the Pygame mixer is stopped before loading new audio
   if pygame.mixer.music.get_busy():
       pygame.mixer.music.stop()

   # Play the audio file
   pygame.mixer.music.load(filename)
   pygame.mixer.music.play()

   while pygame.mixer.music.get_busy():
       pygame.time.Clock().tick(10)

# Create the main window
root = tk.Tk()
root.title("Simple Virtual Assistant")

# Create a heading label
heading_label = tk.Label(root, text="My Virtual Assistant", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=10)

mic_logo_path = "C:/Users/Ang/Desktop/fyp1/mic1.png"  # Replace with the actual path to your mic logo image

# Load mic logo image from a local file using tkinter's PhotoImage
mic_photo = tk.PhotoImage(file=mic_logo_path)

# Resize the image
image_width = mic_photo.width()
image_height = mic_photo.height()

new_width = 60  # New width for the image
new_height = 60  # New height for the image

mic_photo = mic_photo.subsample(image_width // new_width, image_height // new_height)

# Create output text boxes
text_output1 = tk.Text(root, height=5, width=100)
text_output1.pack()

text_output2 = tk.Text(root, height=15, width=100)
text_output2.pack()

# Create a frame for the mic button
mic_button_frame = tk.Frame(root)
mic_button_frame.pack(pady=10)

# Create a small and round mic button with a border
button_width = 75  # Change the button width
button_height = 75  # Change the button height

# Create a small and round mic button
mic_button = tk.Button(
   mic_button_frame,
   image=mic_photo,
   command=mic_button_clicked,
   borderwidth=1,  # Border width
   relief=tk.SOLID,  # Border relief style
   highlightthickness=2,  # highlight on mouseover
   width=button_width,
   height=button_height
)
mic_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
