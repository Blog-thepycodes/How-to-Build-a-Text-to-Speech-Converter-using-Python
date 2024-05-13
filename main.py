from tkinter import *
import pyttsx3
 
 
converter = pyttsx3.init()
 
 
def generate_vocals():
    text = text_entry.get()
    if text:
        converter.say(text)
        converter.runAndWait()
 
 
root = Tk()
root.title("text to speech converter - The Pycodes")
root.geometry("400x200")
 
 
frame = Frame(root)
frame.pack(padx=20,pady=30,fill=BOTH,expand=True)
 
 
label = Label(frame,text="Enter your Text :",font=("Arial",14))
label.pack()
 
 
text_entry = Entry(frame,font=("helvetica",14))
text_entry.pack(padx=10,pady=10,fill=BOTH,expand=True)
 
 
convert_button = Button(frame,text="convert to speech",command=generate_vocals,bg="orange",fg="green",font=("helvetica",14))
convert_button.pack()
 
root.mainloop()
