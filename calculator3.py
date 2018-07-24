#here we are creating a button to a calculator after calculator1.




import tkinter

from tkinter import *

root =Tk() #creats gui window

equa=""  #varible[2.0]

equation=StringVar() #whenver equation chnages calculation label also change using strinvar.[2]

calculation=Label(root, textvariable=equation) #[1].

equation.set("23+3")#[3] call function equatio.set()  and set add example.

calculation.grid(columnspan=4) #merge all 4 column [cause calculator has 4 column buttons]

#each buuton has a root with 0 to 9 button.

def btnPress(num): #every time button press variable [equa] updte with new button value and need to reset equation new bar [1.0]

  global equa  #global varibale we are changing value of equa from[2.0] 

  equa= equa + str(num) # add new no. with str value

  equation.set(equa)

  #button press function

button0=Button(root,text="0", command=lambda:btnPress(0))        #create button0,Lambda function: action[btn name] is an anonyms function


button0.grid(row=4,column=3)

#lamda work like function doesnt require return statement.
#creating 9 button and +,-,%,* button also

button1=Button(root,text="1", command=lambda:btnPress(1))

button1.grid(row=1,column=0)

button2=Button(root,text="2", command=lambda:btnPress(2)) 

button2.grid(row=1,column=1)


button3=Button(root,text="3", command=lambda:btnPress(3)) 

button3.grid(row=1,column=2)

button4=Button(root,text="4", command=lambda:btnPress(4)) 

button4.grid(row=2,column=0)

button5=Button(root,text="5", command=lambda:btnPress(5)) 

button5.grid(row=2,column=1)

button6=Button(root,text="6", command=lambda:btnPress(6)) 

button6.grid(row=2,column=2)

button7=Button(root,text="7", command=lambda:btnPress(7)) 

button7.grid(row=3,column=0)

button8=Button(root,text="8", command=lambda:btnPress(8)) 

button8.grid(row=3,column=1)

button9=Button(root,text="9", command=lambda:btnPress(9)) 

button9.grid(row=3,column=2)

Plus=Button(root,text="+", command=lambda:btnPress("+")) #+
Plus.grid(row=1,column=3)

Minues=Button(root,text="-", command=lambda:btnPress("-")) #-

Minues.grid(row=2,column=3)

Multiply=Button(root,text="*", command=lambda:btnPress("*")) #*

Multiply.grid(row=3,column=3)

Divide=Button(root,text="/", command=lambda:btnPress("/")) #/

Divide.grid(row=3,column=3)

root.mainloop()
