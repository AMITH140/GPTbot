import openai
import pyttsx3
import speech_recognition as sr
#imported the required lib


#initializing voice engine
engine = pyttsx3.init()
engine.setProperty('voice', 'english+f3')
engine.setProperty('rate', 150)
r = sr.Recognizer()
#defining the required/repeated funtions and setting up microphone


def speak(text):
    engine.say(text)
    engine.runAndWait()
with sr.Microphone() as source:
           
        r.adjust_for_ambient_noise(source)
        print("Speak now...")
        speak("speak now please.")
        audio = r.listen(source)
        user_message = r.recognize_google(audio)
        print("YOU SAID-",user_message)
        speak(user_message)
        speak("please wait for 2 minutes so that i can do my research and give you the desired output")

     
#importing api key and asigning it to the openai inbuilt funtion 
API_KEY = open("MYOWNPROJECTS/gptBOT/API.txt","r").read()
openai.api_key = API_KEY

chat_log =[]
while True:
    if user_message.lower() =="quit":
        break
    else:
        chat_log.append({"role":"user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        assistant_response = response["choices"][0]['message']['content']
        print("ATHEENNA:", assistant_response.strip("\n").strip())
        speak(assistant_response)

        chat_log.append({"role":"assistant", "content": assistant_response.strip("\n").strip()})

#so here we have made just the intro that it can input and print out the results and commands but thats not enough
# and we need to use lib like tkinker or anything more advanced that we can find in the net and create  an 
# appealing ui or interface with a option to search for 
# then the next objective is to print out the results
# then the next commit or objective will be how to make the results speak 
# rather than printing out the results we will make the results speak for itself also while showing the output
# in a seperate window using tkinker or something else then after a while we will learn how to implement this in our site
# or maybe a standalone app where you can animate things too 
# thats it for this CHB project and see yo next time in a further more advanced projects #