import pyttsx3
import speech_recognition as sr
import wikipedia
import re
import os
import random
import time
import turtle
import pygame


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("What you want to say")
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def wiki(question):

    try:
        result = wikipedia.summary(question, sentences = 2)
        result = re.sub(r'\([^)]*\)',"", result)#маха ти скобите от сайта
    
        speak(result)
        speak("Thanks for the question!")
                        
    except:
        speak('No information available')
            
def random_student(random):
    with open("Students.txt") as file:
        content = file.readlines()


    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    content= random.choice(content)

    
    turtle.write(content, font=("Arial", 100, "normal"))
    
    turtle.hideturtle()


def play_music(file_mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(file_mp3)
    pygame.mixer.music.play()
    time.sleep(60)
    
def main():
    mp3_file_path = r'C:\Users\Zdravko Anev\OneDrive\Desktop\Programing\Robotika\Lecture01\Other1\V6.mp3'
    play_music(mp3_file_path)
