import speech_recognition as sr
# This Is An External Module To Install This You Need To Use below Command

# pip install SpeechRecognition

def takecommand(): # Voice Input Function 

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(":: Listening....")

        r.pause_threshold = 1 

        audio = r.listen(source)

    try:

        print(":: Recognizing....")

        query = r.recognize_google(audio, language='en-in')

        print(f":: You Said :- {query}\n")

    except:
        return ""
    
    return query.lower()


