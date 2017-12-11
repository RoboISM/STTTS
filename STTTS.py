import speech_recognition as sr 
import pyttsx 
   
 # obtain audio from the microphone  
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty("rate", 120)

with sr.Microphone() as source:  
    print("Say something!")  
    audio = r.listen(source)
   
 # recognize speech using Sphinx  

speech = r.recognize_sphinx(audio)

try:  
    print("This is perhaps what you said '" + speech + "'")  
except sr.UnknownValueError:  
    print("Sorry, couldn't recognize the speech. Please try again.")  
except sr.RequestError as e:  
    print("Error; {0}".format(e))
    
engine.say(speech)
engine.runAndWait()
