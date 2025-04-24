import time
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
#import pywikihow    #search_wikihow(how,max_result,language)
import google.generativeai as gemni
#from pyautogui import *
import pyautogui
import smtplib
#import sys
import pyjokes
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import psutil
import speedtest
import alarm2
import pyaudio
import serial
import Ardino_project

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',180)
#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7, phrase_time_limit=7)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again.....")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    Ardino_project.send_command('h')

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("goodafter noon")
    else:
        speak("good evening")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("goyaladarsh49@gmail.com" , "czyw tchq fwgd gukf")
    print("login succes")
    Ardino_project.send_command('p')
    server.sendmail("goyaladarsh49@gmail.com", to ,content)
    server.close()

def hold():
    e = input("press enter to continue....")
    speak("i am ready to continue , sir")

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=bbc-news&apikey=09c0893433a24c06bb0eaabdd0202d91"
    mainpage = requests.get(main_url).json()
    articles = mainpage["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]
    Ardino_project.send_command('H')
    for ar in articles :
        head.append(ar["title"])
    for j in range(0, 10) :
        print(f"today's {day[j]} news is :{head[j]} ")
        speak(f"today's {day[j]} news is {head[j]}")

def TakeExecution():
    pyautogui.press('esc')
    wish()
    speak("Hii ,I am Sera an bot ,how can i help you sir")
    while True:
    #if 1 :
        query = takecommand().lower()

        # logics building for tasks

        if "open notepad" in query :
            npath = "C:\\Windows\\notepad.exe"
            Ardino_project.send_command('p')
            os.startfile(npath)
        elif "open command prompt" in query :
            Ardino_project.send_command('p')
            os.system("start cmd")
        elif "open camera" in query :
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            Ardino_project.send_command('p')
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27 :
                    break
            cap.release()
            #cv2.distroyALLWindows()

        elif "play music" in query :
            music_dir = "C:\\Users\\goyal\\OneDrive\\Documents\\Desktop\\music\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)

            # 'rd' for random music play put it in to songs[0]
            os.startfile(os.path.join(music_dir, songs[0]))
            Ardino_project.send_command('d')
            hold()

        # for online task
        elif "ip address" in query :
            ip = get('https://api.ipify.org').text
            Ardino_project.send_command('p')
            speak(f"your ip address is {ip}")

        elif "search on wikipedia" in query :
            speak("what should i sarch..")
            query = takecommand().lower()
            results = kit.info(query, lines=2, return_value=True)#wikipedia.summary(query, sentences=2)
            Ardino_project.send_command('H')
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query :
            speak("sir, what should i search on youtube")
            Ardino_project.send_command('l')
            cmy = takecommand().lower()
            kit.playonyt(cmy)
            hold()
            # webbrowser.open(f"https://www.youtube.com/results?search_query={cmy}")

        elif "now dance" in query :
            speak("on which music sir")
            cmy = takecommand().lower()
            kit.playonyt(cmy)
            time.sleep(10)
            Ardino_project.send_command('d')
            hold()


        elif "open facebook" in query :
            Ardino_project.send_command('l')
            webbrowser.open("www.facebook.com")
        elif "open instagram" in query :
            Ardino_project.send_command('l')
            webbrowser.open("www.instagram.com")
            hold()
        elif "open reels" in query:
            Ardino_project.send_command('l')
            speak("you need to enjoy some reels , sir")
            webbrowser.open("https://www.instagram.com/reels/C4zy8poJ2CV/")
            hold()
        elif "open twitter" in query :
            Ardino_project.send_command('l')
            webbrowser.open("www.twitter.com")
        elif "open google" in query :
            Ardino_project.send_command('R')
            speak("sir, what should i search on google")
            cmg = takecommand().lower()
            kit.search(cmg)
            hold()
            # webbrowser.open(f"https://www.google.com/search?q={cmg}")
        elif "open github" in query :
            Ardino_project.send_command('p')
            webbrowser.open("www.github.com")

        elif "send message" in query :
            Ardino_project.send_command('R')
            speak("contact name sir")
            contact = takecommand().lower()
            speak("what , message should i send sir")
            message = takecommand().lower()
            speak("wait few second sir it will take some time")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("user-data-dir=C:/Users/goyal/AppData/Local/Google/Chrome/User Data")
            driver = webdriver.Chrome(options=options)
            driver.get("https://web.whatsapp.com")
            time.sleep(12)
            searchxpath = '//*[@id="side"]/div[1]/div/div[2]/div/div/div/p'
            send_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'
            deliver_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span'
            xpath = f'span[title="{contact}"]'
            driver.find_element("xpath", searchxpath).send_keys("Message")
            time.sleep(6)
            wait = WebDriverWait(driver, 100)
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, xpath))).click()
            time.sleep(2)
            driver.find_element("xpath", send_path).send_keys(message)
            time.sleep(2)
            driver.find_element("xpath", deliver_xpath).click()
            hold()


        elif "send email" in query:
            try:
                Ardino_project.send_command('p')
                speak(" I D , sir")
                to = input("E-mail id: ")
                speak("what should i say")
                content = takecommand().lower()
                sendEmail(to, content)
                speak("E-mail has been  sending.....")

            except Exception as e :
                print(e)
                speak(" sorry sir, E- mail can not be send by some reason")

        elif "find information" in query :
            Ardino_project.send_command('H')
            subject = takecommand().lower()
            speak(kit.info(subject, lines=2, return_value=True))

        elif "set alarm" in query :
            Ardino_project.send_command('R')
            speak("sir please tell me the time to set alarm, for example set alarm to 5:30 a.m.")
            tt = takecommand().lower()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            tt = tt.lstrip(" ")
            print(tt)
            alarm2.alarm(tt)
            hold()


        elif " tell a joke" in query :
            Ardino_project.send_command('p')
            joke = pyjokes.get_joke(language='hi')
            print(joke)
            speak(joke)

        elif "shut down" in query :
            Ardino_project.send_command('l')
            os.system('shutdown /s /t 5')

        elif "restart" in query :
            Ardino_project.send_command('p')
            os.system('shutdown /r /t 5')

        elif "switch the window" in query :
            Ardino_project.send_command('p')
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "show news" in query :
            Ardino_project.send_command('R')
            speak("please wait sir , feaching the latest newses")
            news()

        elif "tell my location" in query :

            speak("wait sir let me Check ")
            Ardino_project.send_command('l')
            try :
                ipad = requests.get("https://api.ipify.org").text
                print(ipad)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipad + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                state = geo_data['region']
                country = geo_data['country']
                speak(f"sir , i am not sure , but i think we are in {city} city of {country} country")
                print(f"sir , i am not sure , but i think we are in {city} city of {country} country")
            except Exception as e :
                speak(" sorry sir , due to network issue i am not able to find where we are ")
                pass

        elif "take a screenshot"  in query or "take a shot" in query :
            Ardino_project.send_command('l')
            speak("sir , please tell me the name of this screen shot")
            name = takecommand().lower()
            speak(" sir , please hold the screen for few second , i am taking a screen shot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(" i am done sir picture is saved in our main folder")

        elif "check temperature" in query or "whether" in query:
            Ardino_project.send_command('l')
            speak("give the city name to know the temperature sir ")
            place = takecommand().lower()
            search = f"temperature in {place}"
            speak("wait few second fetching data")
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(print(f"current{search} is {temp}"))


        elif "hello" in query or "hey" in query:
            Ardino_project.send_command('h')
            speak("may i help you, with something sir.")
        elif "tell me about yourself" in query :
            Ardino_project.send_command('R')
            speak("i am fine ,what about you sir")
        elif "also good" in query or "also well" in query :
            speak("That's great to here from you sir")
        elif "thank you" in query or "thank you for this" in query :
            speak("it's my pleasure sir")
        elif "you can sleep" in query or "sleep now" in query :
            speak("okay sir, i am going to sleep you can call me any time.")
            hold()

        elif "how much power we have" in query or "how much power left" in query or "check battery" in query:
            Ardino_project.send_command('l')
            battery = psutil.sensors_battery()
            percent = battery.percent
            status = f"our system have {percent}% battery"
            print(status)
            speak(status)
            if percent >= 75 :
                speak("we have enough power to continue our work, sir")
            elif percent >= 40 and percent <= 75 :
                speak("we should connect our system to the charger, sir")
            elif percent >= 75 :
                speak("we have enough power to continue our work , sir")
            elif percent >= 15 and percent >= 39 :
                speak("we don't have enough power to work , please connect to the charger, sir")
            elif percent <= 15 :
                speak("we have very low power , please connect to the charger system will shutdown very soon")

        elif "check my internet speed" in query:
            Ardino_project.send_command('l')
            speak('wait few second sir let me check')
            speed = speedtest.Speedtest()
            dl = speed.download()
            dl = int(dl * 0.000000125)
            ul = speed.upload()
            ul = int(ul * 0.000000125)
            x = f"sir we have {dl} MB per second downloading speed and {ul} MB per second uploading speed"
            print(x)
            speak(x)

        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "volume mute" in query:
            pyautogui.press("volumemute")
        elif "now stop" in query:
            hold()
        else:
            x="you want to continue with this question  sir"
            print(x)
            speak(x)
            p = input("y for yes"
                  "n for no:")
            if p == "y":
                gemni.configure(api_key="AIzaSyD9ft-rJ37oj1jVAHSLs4T1uEq9CoGaQNo")
                model = gemni.GenerativeModel('gemini-pro')
                chat = model.start_chat(history=[])
                #speak("ask something")
                #que = takecommand().lower()
                result = chat.send_message(query)
                response = result.text
                response = response.replace("*", "")
                print(response)
            else:
                continue

if __name__ == "__main__":
    Ardino_project.send_command('R')
    time.sleep(2)
    TakeExecution()


