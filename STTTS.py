import speech_recognition as sr 
import pyttsx 
   

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# obtain audio from the microphone  
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty("rate", 120)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  
    print("Say something!")  
    audio = r.listen(source)
   
 # recognize speech using Sphinx 
print ("Done Recording. Analysing Your Speech . . . \n") 

speech = r.recognize_google(audio)

try:  
    print("This is perhaps what you said '" + speech + "'")  
except sr.UnknownValueError:  
    print("Sorry, couldn't recognize the speech. Please try again.")  
except sr.RequestError as e:  
    print("Error; {0}".format(e))
    
engine.say(speech)
engine.runAndWait()
