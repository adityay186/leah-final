import struct
import pyaudio
import pvporcupine
import sys

sys.path.append("/home/aditya/Documents/leah/tts_engine")
sys.path.append("/home/aditya/Documents/leah/intent_engine")
sys.path.append("/home/aditya/Documents/leah/skill_handle")

from intent import get_intent
from skill_handler import process_intent
from googleTTS import GoogleTTS
import speech_recognition as sr
from playsound import playsound

def detect_wake_word():
    porcupine = None
    pa = None
    audio_stream = None

    keys = {
            "adityay186@gmail.com" : "61LuNHOI0Wkh4yBbrkck+HDV39muOqtQF3oevQE3Xt+DhIuiWzo1zg==",
            "20190802060@dypiu.ac.in" : "Zb5nW42pBDH0wOptYTK1neJ1fyrYWPJZv0T0IfkFQKmzXTlQZuo24w=="
    }

    tts = GoogleTTS("")
    r = sr.Recognizer()

    try:
        porcupine = pvporcupine.create(access_key = keys["adityay186@gmail.com"],
                                        keyword_paths = ["hey_leah-linux/hey_leah-linux.ppn"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Wake Word Detected")
                command = None
                with sr.Microphone() as source:
                    print("Speak ...... ")
                    playsound("start_sound.mp3")
                    audio = r.listen(source)
                try:
                    command = r.recognize_google(audio)
                    print(command)
                except sr.UnknownValueError:
                    er = "sorry, could not recognize"
                    tts.text = er
                    print(er)
                    tts.play()
                    continue
                except sr.RequestError as e:
                    er2 = "Could not request results"
                    tts.text = er2
                    print(er2)
                    tts.play()
                    continue

                intention = get_intent(command)
                print(intention)
                res = process_intent(intention)
                tts.text = res
                print(res)
                tts.play()

                
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
                pa.terminate()

detect_wake_word()
