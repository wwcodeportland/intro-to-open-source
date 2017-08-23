import random
import time
responses = ["Not so sure", "Shitty", "Great", "Absolutely not", "Outlook is good", "I see good things happening",
"Never", "Negative", "Could be", "Unclear, ask again", "Yes definitely", "No, Idon't think so"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")

## Following asks user if they would like to play again, and loops until user is finished
query = "Would you like to ask the Wise One a question? Y/N: "
response = (input(query))
while response == str("Y"):
    answerQuery()
    response = (input(query))
else:
    print(input("Press any key to exit"))
