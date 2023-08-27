import pyttsx3
text_speech=pyttsx3.init()
answer=input("please enter your want to convert:")
text_speech.say(answer)
text_speech.runAndWait()
