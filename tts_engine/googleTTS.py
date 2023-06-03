from gtts import gTTS
import pygame
import os

class GoogleTTS:
    def __init__(self, text):
        print("::creating gTTS object::")
        self.language = "en"
        self.text = text

    def play(self):
        # Create a gTTS object
        tts = gTTS(text=self.text, lang=self.language)

        # Save the speech as an MP3 file
        print("::saving audio::")
        tts.save("tts.mp3")

        # Initialize the pygame mixer
        pygame.mixer.init()

        # Load the audio file
        print("::loading audio::")
        pygame.mixer.music.load("tts.mp3")

        # Play the audio
        print("::playing audio::")
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            continue

        # Clean up
        pygame.mixer.quit()
        os.remove("tts.mp3")

