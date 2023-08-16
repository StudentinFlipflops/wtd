from tkinter import * 
from protocol import add_protocol

root = Tk()
root.title("WTD")
root.geometry(f"600x600")


add_button = Button(root , text="add" , padx=10 , pady=10 , command= lambda: add_protocol(root))


add_button.grid(row=0 , column= 0)

root.mainloop()

#Do this things in specific order 


# *** DONE *** #TODO: move fun "add_protocol" and "add_section" to new file
#TODO: add button "save protocol"
#TODO: write the simmplest way to write sections

#INFO: there will be no option for "remove section". Once a protocol is created, ot cannot be modified, it can only be deleted.

# time: 1 week to 17-08-2023
