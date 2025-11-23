import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("600x550")
for i in range (4):

    window.rowconfigure(i,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

#variable
outputvar = tk.StringVar()
massvar = tk.StringVar()
heightvar = tk.StringVar()

#entry
output_entry = ttk.Entry(window,textvariable=outputvar,font=("calibri",30,"bold"))
output_entry.grid(row=0,column=0,columnspan=2,sticky="ewns",padx=20,pady=20)
mass_entry = ttk.Entry(window,textvariable=massvar,font=("calibri",30,"bold"),width=3)
mass_entry.grid(row=1,column=1,sticky="ewns",padx=20,pady=20)
height_entry = ttk.Entry(window,textvariable=heightvar,font=("calibri",30,"bold"),width=4)
height_entry.grid(row=2,column=1,sticky="ewns",padx=20,pady=20)

#label
mass_label = ttk.Label(window,text="ENTER YOUR MASS :(IN KILOGRAM)",font=("calibri",30,"bold"))
mass_label.grid(row=1,column=0,sticky="ewns",padx=20,pady=20)
height_label = ttk.Label(window,text="ENTER YOUR HEIGHT :(IN CENTIMETER)",font=("calibri",30,"bold"))
height_label.grid(row=2,column=0,sticky="ewns",padx=20,pady=20)

#start function
def start():
    m = float(massvar.get())
    h = float(heightvar.get())
    h1 = h/100
    hf = h1 ** 2
    bmi = m / hf
    f = ""
    if(bmi < 18.5):
        f = "Underweight"
    elif(bmi > 18.5 and bmi < 24.9):
        f = "Normal weight"
    elif( bmi > 24.9 and bmi < 29.9):
        f = "Overweight"
    else:
        f = "Obesity"
    outputvar.set(("Your are", f ,"Your BMI is", bmi))

#clear function
def clear():
    outputvar.set("")
    massvar.set("")
    heightvar.set("")

#button
start_button = tk.Button(window,text="START",command=start,font=("calibri",30,"bold"))
start_button.grid(row=3,column=1,sticky="ewns",padx=20,pady=20)
clear_button = tk.Button(window,text="CLEAR",font=("calibri",30,"bold"),command=clear)
clear_button.grid(row=3,column=0,sticky="ewns",padx=20,pady=20)


window.mainloop()