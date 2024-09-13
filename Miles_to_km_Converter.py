from tkinter import *

def converter():
    miles = float(input_miles.get())
    km = round(miles*1.609)
    my_label_km_value.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#LabelMiles
my_label_miles = Label(text="Miles")
# my_label_miles.config(text="Miles")
my_label_miles.grid(column=2, row=0)

# my_label_miles["text"] = "Miles"

#LabelKm
my_label_km = Label(text="0")
# my_label_km.config(text="Km")
my_label_km.grid(column=2, row=1)

my_label_km["text"] = "Km"

#Labelisequalto
my_label_isequalto = Label(text="is equal to")
# my_label_isequalto.config(text="New text")
my_label_isequalto.grid(column=0, row=1)

# my_label_isequalto["text"] = "is equal to"


#Button
button = Button(text= "Calculate", command= converter)
button.grid(column=1, row=2)

#EntryMiles
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

# #EntryKm
# input_km = Entry(width=10)
# input_km.grid(column=1, row=1)

#LabelKmvalue
my_label_km_value = Label(text="0")
my_label_km_value.grid(column=1, row=1)
my_label_km_value["text"] = "0"

window.mainloop()