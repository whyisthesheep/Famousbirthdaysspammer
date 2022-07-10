from turtle import position
import pyautogui
import os
from time import sleep

countdown = 5
input("Press ENTER to start")
for loop in range(countdown):
    countdown = countdown - 1
    print(countdown)
    sleep(1)
os.system("cls")
pyautogui.press("win", "s")
sleep(2.7)
pyautogui.write("chrome")
sleep(2)
pyautogui.press("enter")
sleep(10)
pyautogui.write("https://www.famousbirthdays.com/")
print("you have 15 seconds to go to the page of the person you want to spam")
sleep(3)
os.system("cls")
sleep(12)
countdown = 3
input("Press ENTER and then move your mouse to the boost button")
for loop in range(countdown):
    countdown = countdown - 1
    print(countdown)
    sleep(1)
location = pyautogui.position()
os.system("cls")
print("Press CTRL + C in terminal to end it")
sleep(3)
os.system("cls")
while countdown != 0:
    pyautogui.press("ctrl", "r")
    sleep(3)
    pyautogui.click(position)
    print("Clicked at " + position)
    sleep(2)
