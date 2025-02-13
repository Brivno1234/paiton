import emsine as esimenefail
import teine as teineFail
import kolmas as kolmasFail

userInput = input("Miline ülesanne sa tahan ülevaadata")
if userInput =="1":
    esimeneFail.MyFunc()
elif userInput =="2":
    from pykkar import *
    create_world("""
    ########
    #  >   #
    #      #
    #      #
    #      #
    #      #
    ########
    """)
for i in range(25):
        if is_painted() == False:
            if is_wall() == True:
                right()
            paint()
            step()
for i in range(10):
    if is_painted() == True:
        right()
    paint()
    step()
for i in range(2):
        if is_painted() == False:
             paint()
        step()
for i in range(9):
    if is_painted() == True:
        right()
    paint()
    step()
   

    
else:
    pass