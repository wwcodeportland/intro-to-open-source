import random
import time
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Ask and you shall receive: ")
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else:
    print(input("Press any key to exit"))