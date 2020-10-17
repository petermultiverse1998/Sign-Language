import pyttsx3

def speak(text):
    voice_id_f = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    #voice_id_m = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine = pyttsx3.init()
    engine.setProperty('rate', 108)
    engine.setProperty('volume', 0.9)
    engine.setProperty('voice', voice_id_f)
    engine.say(text)
    engine.runAndWait()

def voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:  
        print("Voice:") 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages) 
    
speak('I am peter multiverse')
voices()