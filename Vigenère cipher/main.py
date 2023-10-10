from tkinter import *
from tkinter import filedialog
from encryption import *
from key_generation import *
#window setup
window = Tk()
window.geometry("720x520")
window.title("Vigenère cipher")
window.config(background="#FAF398")

KEYpath="Vigenère cipher/key/key.txt"
def selectpath():
    global KEYpath
    Tk().withdraw() # prevents an empty tkinter window from appearing
    KEYpath= filedialog.askopenfilename()

#title
title = Label(window,text="Vigenère cipher",
              font=("Algerian",20,'bold'),
              background="#FAF398")
title.place(x=5,y=5)

#ciphertext textbox setup
ciphertext = Text(window, 
                 font=(10),
                 height=10,
                 width=62)
ciphertext.place(x=5,y=50)
#plaintext textbox setup
plaintext = Text(window, 
                 font=(10),
                 height=10,
                 width=62)
plaintext.place(x=5,y=270)

#encrypt button set up
enbutton = Button(window,text="encrypt",
                  command=lambda: encrypt_click(ciphertext,plaintext,KEYpath))
enbutton.place(x=600,y=150)
#decrypt button set up
debutton = Button(window,text="decrypt",
                  command=lambda: decrypt_click(plaintext,ciphertext,KEYpath))# Not finished
debutton.place(x=600,y=350)
#create key text file in the folder
GenKey = Button(window,text="generate key",
                command=lambda: generation())
GenKey.place(x=600,y=275)

selectPath = Button(window,text="import key",
                    command=lambda: selectpath())
selectPath.place(x=600,y=315)
window.mainloop()