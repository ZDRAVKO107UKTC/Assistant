from Funcions import wiki
from Funcions import speak
from Funcions import recognize_speech
from Funcions import random_student
from Funcions import play_music
from Funcions import main
import time
import re
import os
import daytime
import random
import turtle
import pygame       


if __name__ == '__main__':
    while True:
        question=recognize_speech()
        time.sleep(5)

        if "bye" in question:
            speak("bye bye daddy")
            break

        elif "search" in question or "how" in question:
            wiki(question)
            continue

        elif "folder" in question:
            user_input = recognize_speech()
            os.mkdir(user_input)
        
        elif "engine" in question:
            main()
            continue
        
        
        elif "shut down" in question:
            os.system('shutdown /s /t 1')
        
        elif "random student" in question:
           turtle.speed(1)

           (random_student(random))
           
           turtle.done()
        
