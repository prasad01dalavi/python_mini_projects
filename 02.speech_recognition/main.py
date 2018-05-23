import speech_recognition as sr

record_audio = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something!')
    audio = record_audio.listen(source)  # listen from the mic source

try:
    print('You said', record_audio.recognize_google(audio))
except:
    print('Error occurred!')
    pass

pip install SpeechRecognition
pip install pyaudio
