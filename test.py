# import requests
# import json
# import pyttsx3
# import speech_recognition as sr
# import re
# def get_audio():
# 	r = sr.Recognizer()
# 	with sr.Microphone() as source:
# 		audio = r.listen(source) # record the audio
# 		said = ""

# 		try: 
# 			said = r.recognize_google(audio)
# 		except Exception as e:
# 			print('Exception:', str(e))
	
# 	return said.lower()

# def main():
# 	print("Started program")
# 	while True:
# 		print("Listening...")
# 		text=get_audio()
# 		print(text)
# 		break
# 		result=None

# main()
