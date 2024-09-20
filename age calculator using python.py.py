import  tkinter as tk
from datetime import datetime
from tkinter import messagebox 


def calculate_age():
	try:
		name = (entry_name.get())
		birth_day = int(entry_day.get())
		birth_month = int(entry_month.get())
		birth_year = int(entry_year.get())
		
		today = datetime.today()
		age = today.year - birth_year -((today.month , today.day)<(birth_month , birth_day))
		
		messagebox.showinfo("Age" ,
f"{name} , Your age is : {age}  years ")
		
	except ValueError :
		messagebox.showerror("Invalid input" , "Please enter a valid numeric values. ")
		

		

root = tk .Tk()
root.title("AGE CALCULATOR")


label_name = tk.Label(root , text = "NAME")
label_name.grid(row = 0 , column = 0 , padx = 10 , pady = 10)
entry_name = tk.Entry(root)
entry_name.grid(row = 0 ,column = 1, padx = 10, pady = 10)

label_day = tk.Label(root , text =" DAY OF BIRTH" )
label_day.grid( row = 1 , column = 0 , padx = 10 , pady = 10)
entry_day = tk.Entry(root)
entry_day.grid( row = 1 , column = 1 , padx = 10 , pady = 10)

label_month = tk.Label(root , text = "MONTH OF BIRTH")
label_month.grid(row = 2, column = 0, padx = 10 , pady = 10)
entry_month = tk.Entry(root)
entry_month.grid(row = 2 ,column = 1, padx = 10 , pady = 10 )

label_year = tk.Label(root , text = "YEAR OF BIRTH")
label_year.grid(row = 3 , column = 0, padx = 10 , pady = 10)
entry_year = tk.Entry(root)
entry_year.grid(row = 3, column = 1 , padx = 10 , pady = 10)


button_calculate = tk.Button(root , text =  " Calculate Age " , command = calculate_age)
button_calculate.grid(row = 4 , columnspan = 2 , padx = 20 , pady = 20)


root.mainloop()



 