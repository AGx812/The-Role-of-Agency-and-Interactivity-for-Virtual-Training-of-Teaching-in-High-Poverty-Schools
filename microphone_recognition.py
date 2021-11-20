# by ABDULLAH GHANIMA

from rasa_virtual_agent_master.Devs.rasaAPI import main

# import sys
# sys.path.append("**C:\Users\abdul\OneDrive\Desktop\ARESTY\SpeechToText\rasa_virtual_agent_master\Devs**")
# from rasaAPI import main



# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        var = r.recognize_google(audio);
        
        # print("Google Speech Recognition thinks you said: " + var)

        # rasa does not exit until /stop is called, we need to find a way for RASA to force exit
        # after one response is computed, or it might be more effective if we place the STT into RASA

        main(var)

        # print("test")



        # send var to RASA, and it will return some output
        # print that output
        

        # if var == "stop":
        #     break
        # elif var == "I am doing well":
        #     print("RESPONSE: that is good to hear. did you do the homework")
        # elif var == "yes I completed it":
        #     print("RESPONSE: good job")
        # elif var == "hello" or "hi" or "how are you":
        #     print("RESPONSE: hello, how are you")


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
