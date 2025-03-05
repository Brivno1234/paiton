def addtext(piton, text):
    text = input("ведите текст")
    with open(piton, "a", encoding="utf-8") as file:  
        file.write(text + "\n")  
addtext("piton.txt", "добавлено")
