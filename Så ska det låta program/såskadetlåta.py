from tkinter import *

# ---------------------------------fönster---------------------------------



settings_win = Tk()
settings_win.title("Settings")
settings_win.geometry("600x400+0+100")

quiz_win = Toplevel()
quiz_win.title("Så ska det låta quiz")
quiz_win.geometry("1200x675+650+200")

bg = PhotoImage(file = "apeter.png")
bgl = Label(quiz_win, image = bg, height=1080, width=1920)
bgl.image = bg
bgl.place(x=0, y=0)


bSizeX = 38
bSizeY = 15

lSizeX = 11
lSizeY = 4

wLocY = 650
wOffsetX = 300

tSize = 30

# ---------------------------------END fönster---------------------------------
# ---------------------------------Lyrics---------------------------------

i = 0.13
ri = 1

def reset():
  global i
  global ri
  i = 0.13
  ri = 1

Reset = Button(settings_win, text="Reset", command=lambda:reset())
printiri = Button(settings_win, text="print", command = lambda: [print(i), print(ri)])

def forget_wid(wid):
  wid.pack_forget()

def create_word_white(word):
  global ri
  b = Button(quiz_win, height = bSizeY, width = bSizeX, bg = "white", text = ri, command = lambda: [forget_wid(b), 
    Label(quiz_win, font=("Comic Sans MS", tSize), text = word, height = lSizeY, width = lSizeX, bg = "white").place(x = b.winfo_x(), y = wLocY)])

  global i
  b.place(x = i*wOffsetX, y = wLocY)
  i += 1
  ri += 1

def create_word_red(word):
  global ri
  b = Button(quiz_win, height = bSizeY, width = bSizeX, bg = "white", text = ri, command = lambda: [forget_wid(b), 
    Label(quiz_win, font=("Comic Sans MS", tSize), text = word, height = lSizeY, width = lSizeX, bg = "red3").place(x = b.winfo_x(), y = wLocY)])

  global i
  b.place(x = i*wOffsetX, y = wLocY)
  i += 1
  ri += 1
  

def Word_input_white(text):
    INPUT = text.get("1.0", "end-1c")
    print(INPUT)
    create_word_white(INPUT)

def Word_input_red(text):
    INPUT = text.get("1.0", "end-1c")
    print(INPUT)
    create_word_red(INPUT)
     
l = Label(text = "input word WHITE")
Word = Text(settings_win, height = 1,
                width = 25,
                bg = "white")

Add_White = Button(settings_win, height = 2,
                 width = 20,
                 text ="Add word WHITE",
                 command = lambda:Word_input_white(Word))

l2 = Label(text = "input word RED")
Word_Red = Text(settings_win, height = 1,
                width = 25,
                bg = "red3")
 
Add_Red = Button(settings_win, height = 2,
                width = 20,
                text ="Add word RED",
                command = lambda:Word_input_red(Word_Red))


# ---------------------------------END lyrics---------------------------------
# ---------------------------------bilder---------------------------------

# chad = PhotoImage(file = "")

# bilder = [chad, chad, chad, chad, chad, chad]

# def bilder():

#   for ri in range(1, 6):
#     b = Button(quiz_win, height = bSizeY, width = bSizeX, bg = "white", command = lambda: [forget_wid(b), 
#         Label(quiz_win, height = lSizeY, width = lSizeX, image=chad).place(x = b.winfo_x(), y = wLocY)]).place(x = (ri)*wOffsetX, y = wLocY)
#     # b.place(x = i*wOffsetX, y = wLocY)

  

# bilder = Button(settings_win, text="bilder1", command = bilder())

# ---------------------------------END bilder---------------------------------

Quit = Button(settings_win, text="Quit", command = settings_win.destroy)

l.pack()
Word.pack()
Add_White.pack()

l2.pack()
Word_Red.pack()
Add_Red.pack()

Quit.pack(side = BOTTOM)
Reset.pack(side = BOTTOM)
printiri.pack(side = BOTTOM)
# bilder.pack(side = BOTTOM)


settings_win.mainloop()