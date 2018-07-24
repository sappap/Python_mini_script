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


button0.grid(row=1,column=0)

#lamda work like function doesnt require return statement.

button1=Button(root,text="1", command=lambda:btnPress(1))

button1.grid(row=1,column=1)

button2=Button(root,text="2", command=lambda:btnPress(2)) 

button2.grid(row=1,column=2)

root.mainloop()
