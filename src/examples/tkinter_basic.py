from tkinter import *
from tkinter import filedialog as fd;

# window basics
window = Tk()
window.title("Basic example!")
window.geometry('400x300')

# create label widget
lbl = Label(window, text="Label text", font=("Arial Bold", 32))
lbl.grid(column=0, row=0) # grid layout at position (0, 0)

# sent to button 
def clicked_cb():
    filename = fd.askopenfilename(title='Select CSV file to plot')

# create button widget
btn = Button(window, text='get file name', command=clicked_cb)
btn.grid(column=1, row=0)

window.mainloop()

