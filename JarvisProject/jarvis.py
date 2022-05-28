import random
import time
import webbrowser
import psutil
import pyttsx3
import pywhatkit
import requests      # use for tempreture...
import speech_recognition as sr
import pyaudio
import datetime
import pywikihow  # for related to making...
import os
import cv2
import random
from requests import get ###.......for the ip address....
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import pyjokes     #for make a joke..
import pyautogui   #for send whatapp sms
import instaloader
import psutil as ps  # This for the Battery check...
from bs4 import BeautifulSoup
from googletrans import Translator          # use for google translate
from pywikihow import search_wikihow        # related to cook
import operator                       # for calculation...

##############>...........These are for GUI............<##############
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGui import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',200)


# text to speech


def Speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

###########...........wish Me any time..........##############
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour <= 12:
        Speak(f"Good morning sir, CurrentTime is {tt}")
    elif hour > 12 and hour < 18:
        Speak(f"Good afternoon sir, CurrentTime is {tt}")
    else:
        Speak(f"Good Evenining sir, CurrentTime is {tt}")

    Speak("I am jarvis sir, please tell me how may i help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExe()

    # To convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print("Listening.........")
            r.pause_threshold = 1
            r.energy_threshold = 3500
            audio = r.listen(source)
        try:
            print("Recognizing........")
            query = r.recognize_google(audio, language= 'en-in')
            #print(query)
            print(f"user said: {query}")
        except Exception as e:
            Speak("say that again please sir.......")
            return "none"
        return query.lower()

    # Speak("hello sir i am jarvis")

    def TaskExe(self):

        def celcius():
            search = "temperature in jabalpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            Speak(f"The temperature Outside is {temperature} celcius")


        def Whatsapp():
            Speak("Tell Me The Name Of the Person!")
            Speak("Tell Me The Message!")
            msg = self.takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour!")
            hour = int(self.takecommand())
            Speak("Time In Minutes!")
            min = int(self.takecommand())
            pywhatkit.sendwhatmsg("+918103334932", msg, hour, min, 20)
            Speak("Ok Sir, Sending Whatsapp Message!")

        ############.............sena Email..............#############
        def sendEmail(to, content):
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("kushwahaashokkumar439@gmail.com", "Ashok@2002")
            server.sendmail("abhishekkumarku2001@gmial.com", to, content)
            server.close()

        wish()

        while True:

            self.query = self.takecommand()
            if "open notepad" in self.query or "open notepad for me" in self.query:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path)
    
            elif "open command prompt" in self.query:
                os.system("start CMD")
    
            elif "who are you" in self.query:
                Speak("hello sir my name is jarvis! your close friend")
    
            elif "what is your name" in self.query:
                Speak("my name is jarvis and your friend")
    
            elif "hello jarvis" in self.query:
                Speak("hello sir, How are you..?")
    
            elif "i am good and you" in self.query:
                Speak("i am also good sir...!")
    
            elif "jarvis how are you" in self.query or "how are you jarvis" in self.query:
                Speak("I am fine sir, what's about you?")
    
            elif "i am also fine" in self.query or "i am also good" in self.query:
                Speak("ok sir")
    
            elif "jarvis you are stupid" in self.query:
                Speak("Sorry sir, but whats my misstek")

            elif"what is my name" in self.query:
                Speak("sir i think!, You are ashok kumar")

            
            elif "write down" in self.query:
                Speak("what should i write down sir.")
                note = self.takecommand()
                remember = open("data.txt", 'w')
                remember.write(note)
                remember.close()
                Speak(f"I have notes that {note}")


            elif "play music" in self.query or "play gana"  in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))


            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k =cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()


            elif "what is my ip address" in self.query:
                ip = get('https://api.ipify.org').text
                Speak(f"your ip address is {ip}")

            elif "how much power we have" in self.query or "how much power left" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                Speak(f"sir our system have {percentage} percent battery")
                if percentage >=75:
                    Speak("sir we have enought power to continue our work")
                elif percentage>=40 and percentage<=75:
                    Speak("sir we should connect our system to charging point")
                elif percentage<=15 and percentage<=39 :
                    Speak("sir we don't have a enought power to work, please connect to charging")
                elif percentage<=15:
                    Speak("sir we have very low power, please connect with charging otherwise system will shutdown very sonn!")


            elif "wikipedia" in self.query:
                Speak("searching wikipedia....")
                query = self.query.replace("wikipedia..","")
                results = wikipedia.summary(self.query,sentences = 3)
                Speak("according to wilipedia.......")
                Speak(results)
                print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")
                Speak("open sir.")

            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")


            elif "open google" in self.query:
                Speak("sir what you want to surch on google🤨 ")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send message"  in self.query:
                kit.sendwhatmsg("+919302280568","hello how are you i was send message for testing..",2,25)

            elif "play songs on youtube" in self.query or "youtube me songs chalao" in self.query or "songs play on youtube" in self.query:
                Speak("Tell me the NamE of Song...!")
                mn = self.takecommand()
                kit.playonyt(mn)


            elif 'google search' in self.query:

                query = self.query.replace('google search', '')
                Speak('searching on google')
                webbrowser.open("https://www.google.com/search?q=" + query + "&rlz=1C1CHZN_enIN949IN949&oq=" + query +
                                "&aqs=chrome..69i57j0i131i433j0i433j0i131i433l3j0i433j0i131i433j0i433j0.2513j0j15&sourceid=chrome&ie=UTF-8")

            elif "I am where" in self.query or "where is" in self.query:
                query = self.query.replace('where is', '')
                location = query
                Speak('serching' "" + location + "" 'on maps')
                webbrowser.open("https://www.google.co.in/maps/place/" + location + '')
                Speak("Serching" + location)

            # switch the window
            elif "switch the window" in self.query or "switch window" in self.query:
                Speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")


            elif "send mail" in self.query:
                try:
                    to = "abhishekkumarku2001@gmial.com"
                    Speak("what you want send Email")
                    content = self.takecommand().lower()
                    sendEmail(to, content)
                    Speak("Email has been sent to ashok")
                except Exception as e:
                    print(e)
                    Speak("sorry sir i am not able to send Email to ashok")


            elif 'open java point' in self.query:
                Speak("Ok Sir!")
                webbrowser.open("https://www.javatpoint.com")
                Speak("Ok Sir....")



            elif 'play music' in self.query:
                music = 'E:\\Music'
                songs = os.listdir(music)
                os.startfile(os.path.join(music, songs[0]))

            elif 'wikipedia' in self.query:
                Speak("Searching wikipedia.....")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                print(wiki)
                Speak(f"According to wikipedia : {wiki}")

            elif "temperature in jabalpur" in self.query:
                celcius()


            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                Speak(joke)


            #######################################################################################################################
            #######################################################################################################################

            elif "do some calculationns" in self.query or "can you calculate" in self.query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        Speak("Say What you want to calculate, example : 3 plus 3")
                        print("Listening......")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+': operator.add,  # plus
                            '-': operator.sub,  # minus
                            'x': operator.mul,  # multiplied by
                            'divided': operator.__truediv__,  # divided
                        }[op]

                    def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)

                    Speak("your result is")
                    Speak(eval_binary_expr(*(my_string.split())))

                except Exception as error:
                    Speak("try again")
                    return "none"


            ###########>.............all about made...............<##############
            elif "activate how to do mode" in self.query:
                Speak("How to do mode is activated")
                while True:
                    Speak("please tell me what you want to know?")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            Speak("Okey sir, how to do mode is closed")
                            break
                        else:
                            max_result = 1
                            how_to = search_wikihow(how, max_result)
                            assert len(how_to) == 1
                            how_to[0].print()
                            Speak(how_to[0].summary)
                    except Exception as error:
                        Speak("sorry sir, i am not able to find this.")

                ##################################################################################################################

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")
    
            elif "restart the system" in self.query or "restart my laptop" in self.query:
                os.system("shutdown /r /t 5")
    
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif"no thanks" in self.query:
                Speak("okey sir! Thank you for Using me.")
                sys.exit()
            
            elif "you can sleep now" in self.query:
                Speak("okey sir, I am going to sleep you can call me anytine.")
                sys.exit()
    
            Speak("sir do you have any other work")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/jarvis Gui/Jarvis_Gui (2).gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())


