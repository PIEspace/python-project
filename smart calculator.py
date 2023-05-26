# making a smart calculator using python 

import pyttsx3
import datetime

engine = pyttsx3.init()
# set the voice rate 
engine.setProperty('rate' , 125 )

# set the datatetime
hour = int (datetime.datetime.now().hour)

# create a function for pyttsx3 module
def speak(myvoice):
    engine.say(myvoice)
    engine.runAndWait()


# defne the datatetime 

def mytime ():

    # using a if-else statement
    if hour>=0 and hour<12:
        speak("good morning sir ")
        print ("good moring sir ")

    elif hour >=12 and hour<18:
        speak("good afternoon sir")
        print("good afternoon sir ")

    else :
        speak("good night sir ")
        print ("good night sir")

mytime()

# define the calculator 
for robot in range (10000):
    speak("welcome to smart calculator")

    # define the cal value 
    speak("enter the calculator value")
    cal = input("enter the calculator value = '+' ,'-' ,'*' ,'/' ")
    speak(cal)

    # define the two value input from the user 
    speak("enter the first value ")
    number1 = int (input("enter the first number "))
    speak(number1)

    # define the second number
    speak("enter the second number")
    number2 = int (input("enter the second number"))
    speak(number2)

    # now using a if-else statement
    if(cal == '+'):
        speak("this is a add value ")
        add = number1 + number2
        print("the value of sum is = " , add )
        speak(add)
        speak("thank you sir have a nice day")

    elif(cal == '-'):
        speak("this is a subtract value")
        sub = number1 - number2 
        print ("the value of subtract is = " , sub)
        speak(sub)
        speak("thank you sir have a nice day ")

    elif(cal == '*'):
        speak("this is a multiple value ")
        mul = number1 * number2 
        print ("the value of multiple is  " , mul)
        speak(mul)
        speak("thank you sir have a nice day")

    elif(cal == '/'):
        speak("this is a divide value")
        div = number1 / number2 
        print ("this is  a divide value " , div)
        speak(div)
        speak("thank you sir have a nice day ")



    
