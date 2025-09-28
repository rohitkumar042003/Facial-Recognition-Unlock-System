#import module from tkinter for UI
from tkinter import *
# from playsound import playsound
import os
# from datetime import datetime;
#creating instance of TK
root = Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    os.system("python Facial_Recognition_Part1_Capture_Sample.py")
    
def function2():
    os.system("python Facial_Recognition_Part2_Train_Model.py")

def function3():
    os.system("python Facial_Recognition_Part3_Recognition.py")

def function4():
    os.system("python Show_Samples.py")

def function5():    
   os.startfile(os.getcwd()+"/developers/Developer.html");
   
def function6():

    root.destroy()

# def attend():
    # os.startfile(os.getcwd() + "/developers/dietslideshow.html");

#stting title for the window
# root.title("AUTOMATIC FACE UNLOCK SYSTEM USING FACE RECOGNITION")


#creating a text label
Label(root, text="AUTOMATIC FACE UNLOCK SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset/Capture Samples",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Show Samples / Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function4).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Unlock",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
# Button(root,text="Automatic Face Unlock Technology",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Developers",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
