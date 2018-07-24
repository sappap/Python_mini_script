#need to add lable into your GUI screen.

#Label is like a variable 'Label(root window,text="xyx")'#create widget

#need to add 'packet' function to a widget.

from tkinter import *

root=Tk() #root to create window

label1=Label(root,text="this is a tkinter window") #creats label in root window of GUI with text

label2=Label(root,text="this is a tkinter second window message") #creats label in root window of GUI with text

label1.pack() #to call .pack() function to display label1 on root window

label2.pack() #to call .pack() function to display label2 on root window

root.mainloop()

