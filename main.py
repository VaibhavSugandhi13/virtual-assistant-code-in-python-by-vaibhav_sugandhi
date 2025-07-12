 # an Virtual_environment is used for making the project  
import pyttsx3 # it is the module that is used to convert the text to speech
import speech_recognition as sr # it is the module that is  used to convert speech to the text and here we are sustituting as sr so we can use it by enter ing sr only
import webbrowser # it is used to access web browser for any searching
import pyjokes # it is used to get jokes if user has ask to share a jokes
import datetime # it is used to get the date and time {current}
import time # it is used to set the tiime interval of lapping like things
import openai # it is just called but we can not use it  because we have to use the api key for it 




# Function to convert text to speech  by pyttsx3
def speechtext(x): # function is define and  x is a attribute ask by him
    engine = pyttsx3.init()  # here a engine is object and pyttsx3 is a module name and init is used for the class
    voices = engine.getProperty('voices')  # it is used for translating the text into the sppech
    engine.setProperty('voice', voices[0].id)  # i am just using a 0 for the men voice and at the place of the 0 i can replace it with the 1 for the female voice
    engine.setProperty('rate', 125) # adjusting the rate of the voice
    engine.say(x) # calling the funnction and giving him a string to connversion
    engine.runAndWait()

# Function to capture speech from microphone
def sptext(): #  here a sptect is a function that i have define for the conversion for the speech to the text
    recognizer = sr.Recognizer() # recognizer is a object and after the equal to ssign the sr is a module name and a Recognizer is a class
    with sr.Microphone() as source: # now we are using the microphone to get the user input via voice
        print(" Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1) # to avoid the unwanted noise , polluted free voice
        time.sleep(1) # jusr for time lapping for  1 second 
        try: # here a exceptional handling is done 
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            print(" Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f" You said: {data}")
            return data.lower()
        except sr.WaitTimeoutError:
            print(" No speech detected.")
            return ""
        except sr.UnknownValueError:
            print(" Could not understand.")
            return ""
        except sr.RequestError:
            print(" API unavailable.")
            return ""

# Main program loop
if __name__ == "__main__":
    speechtext("Voice assistant activated. Say 'Hey Google' to begin.")
    
    while True:
        wake = sptext() # it is used for the converting the user input via voice into a text
        print("🔍 Wake word recognized:", wake)

        # Exit condition
        if any(word in wake for word in ["exit", "stop", "stop listening", "quit", "bye"]):
            speechtext("Okay, exiting now. Goodbye!")
            break

        # Wake word check
        if any(word in wake for word in ["hey google", "google", "hi google", "hello google"]):
            speechtext("Yes, I am listening.")
            data1 = sptext()
            print("📥 Command received:", data1)

            if "name" in data1:
                speechtext("My name is Google.")
            elif "founder" in data1 or "who owns you" in data1:
                speechtext("My owner is Vaibhav Sugandhi.")
            elif "time" in data1 or "date" in data1:
                current_time = datetime.datetime.now()
                speechtext(f"The current time is {current_time}")
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com")
                speechtext("Opening YouTube.")
            elif "linkedin" in data1:
                webbrowser.open("https://www.linkedin.com")
                speechtext("Opening LinkedIn.")
            elif "chrome" in data1:
                webbrowser.open("https://www.google.com")
                speechtext("Opening Google Chrome.")
            elif "whatsapp" in data1:
                webbrowser.open("https://web.whatsapp.com")
                speechtext("Opening WhatsApp.")
            elif "vtop" in data1:
                webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/login")
                speechtext("Opening VTOP.")
            elif "instagram" in data1:
                webbrowser.open("https://www.instagram.com")
                speechtext("Opening Instagram.")
            elif "facebook" in data1:
                webbrowser.open("https://www.facebook.com")
                speechtext("Opening Facebook.")
            elif "twitter" in data1 or "x" in data1:
                webbrowser.open("https://www.twitter.com")
                speechtext("Opening Twitter.")
            elif "amazon" in data1:
                webbrowser.open("https://www.amazon.in")
                speechtext("Opening Amazon.")
            elif "flipkart" in data1:
                webbrowser.open("https://www.flipkart.com")
                speechtext("Opening Flipkart.")
            elif "spotify" in data1:
                webbrowser.open("https://open.spotify.com")
                speechtext("Opening Spotify.")
            elif "netflix" in data1:
                webbrowser.open("https://www.netflix.com")
                speechtext("Opening Netflix.")
            elif "chatgpt" in data1 or "openai" in data1:
                webbrowser.open("https://chat.openai.com")
                speechtext("Opening ChatGPT.")
            elif "joke" in data1:
                joke = pyjokes.get_joke()
                speechtext(joke)
            elif "krishna" in data1 or "kr$na" in data1 or "me i guess" in data1 or "play me i guess" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=eqzjntKYvHc")
                speechtext("Playing Me I Guess by KR dollar NA.")
            elif "humsafar" in data1 or "play humsafar" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=vY7RaQUmzmY")
                speechtext("Playing Humsafar by Akhil Sachdeva.")
            elif (
                "jo tu mere paas hai" in data1 
                or "jo tum mere ho" in data1 
                or "anuv jain" in data1 
                or "anup jain" in data1 
                or "pramod jain" in data1
            ):
                webbrowser.open("https://www.youtube.com/watch?v=ilNt2bikxDI")
                speechtext("Playing Jo Tu Mere Paas Hai by Anuv Jain.")
            elif "play" in data1 and "youtube" in data1:
                song = data1.replace("play", "").replace("on youtube", "").strip()
                if song:
                    speechtext(f"Searching YouTube for {song}")
                    search_query = song.replace(" ", "+")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                else:
                    speechtext("What song would you like me to search on YouTube?")
                

            
    
            
            
            else:
                speechtext("I don't know that. Let me search it on Google for you.")
                search_query = data1.replace(" ", "+")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

        else:
            print(" Wake word not detected.")
