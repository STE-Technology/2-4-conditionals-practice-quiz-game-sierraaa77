"""
File: quiz.py
Author: Sierra Lunardon
Date: 2024-03-05
Description: This program asks the user questions, checks their answers, then outputs users final scoore.
"""

#print title
print("Mutilpe-Choice Quiz Game")

#Beginning Score
score = 0

#Question 1
print("1. What is the capital of France?")
print("(a) Paris")
print("(b) London")
print("(c) Rome")
answer=input()
if answer == "a" or answer == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#Question 2
print("2. Which planet is known as the Red Planet?")
print("(a) Mars")
print("(b) Venus")
print("(c) Juipter")
answer = input()
if answer == "a" or answer == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#Question 3
print("3. Who painted the Mona Lisa?")
print("(a) Leoardo da Vinci")
print ("(b) Pablo Piasso")
print("(c) Vincent van Gogh")
answer = input()
if answer == "a" or answer == "A":
    print("Correct!")
    score += 1
else: 
    print("Incorrect.")

#calculate percentage
percentage = (score/3) * 100

#Output Users Score
print("Quiz Complete!")
print("You answered" ,score, "out of 3 questions correctly. Your score is"  ,int(percentage), "%.")