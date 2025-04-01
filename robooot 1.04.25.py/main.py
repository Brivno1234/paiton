import esimeneFail
import teineFail

userInput = input("Miline ülesanne sa tahan ülevaadata: ")

if userInput == "1":
    esimeneFail.MyFunc()
elif userInput == "2":
    teineFail.Run_task()
else:
    print("Tundmatu ülesanne.")
