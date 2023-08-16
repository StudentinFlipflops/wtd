from tkinter import * 
from tkinter import messagebox
import csv


def add_section(app , monitor , workspace , section , window , n ):



    section.append([app.get() , monitor.get()  , workspace.get() , 0 ])

    # Each time you press the "name" button, it iterates through the list and generates messages from the beginning .
    # This code needs an uptade in the future.

    for x in section:
        Message(window , text=x[0] , width=100).grid(row = n , column=0)
        Message(window , text=x[1] , width=100).grid(row = n , column=1)
        Message(window , text=x[2] , width=100).grid(row = n , column=2)
        n+=1

    app.delete(0 , END)
    monitor.delete(0 , END)
    workspace.delete(0 , END)
    #print(section)


    

def save_protocol(list , input, window):
    
    if(len(list) == 0):
        messagebox.showinfo("Sectiond not found","Pleas ensure that you add a section. \nYou cannot save an empty protocol." )
    
    else:
        if(input.get() == ""):
            messagebox.showinfo("Protocol name not found","Pleas ensure that you type protocol name. \nYou cannot save an protocol withut name." )
        else:   

            file_name = input.get() +".csv"
            input.delete(0 , END)

            with open(  file_name ,mode ='w' , newline=""  ) as file:
                csv_writer = csv.writer(file)

                for row in list:
                    csv_writer.writerow(row)
                    window.destroy()

            messagebox.showinfo("Protocol saved","protocol saved successfully." )





def add_protocol(root):

    add_protocol_window = Toplevel(root)
    add_protocol_window.title("Second Window")

    #creating a list to collect all data about a specific section. 
    #The variable "n" represents the row in which the message about the section should be displayed. 
    section_list= []
    n= len(section_list)+2

    protocol_name_mess = Message( add_protocol_window , text="Please enter the protocol name:"  , width=250)
    protocol_name_input = Entry( add_protocol_window  , borderwidth=2)

    section_app         = Message(add_protocol_window , text="App to run:" , width=100)
    section_monitor     = Message(add_protocol_window , text="monitor:" , width=100)
    section_workspace   = Message(add_protocol_window , text="workspace:" , width=100)

    section_entry_app           =Entry(add_protocol_window , width=30 , borderwidth= 2)
    section_entry_monitor       =Entry(add_protocol_window , width=30 , borderwidth= 2)
    section_entry_workspace     =Entry(add_protocol_window , width=30 , borderwidth= 2)
    
    section_add_button          =Button(add_protocol_window , text="Add section" , command= lambda:
        add_section(section_entry_app , section_entry_monitor , section_entry_workspace , section_list , add_protocol_window , n))

    section_save_button         =Button(add_protocol_window , text="Save protocol" , command= lambda: 
        save_protocol(section_list , protocol_name_input , add_protocol_window))


    protocol_name_mess.grid(row=0 , column=0)
    protocol_name_input.grid(row=0 , column=1)


    
    section_app.grid(row=1 , column=0)
    section_monitor.grid(row=1 , column=1)
    section_workspace.grid(row=1 , column=2)


    section_entry_app.grid(row=50 , column=0)
    section_entry_monitor.grid(row=50 , column=1)
    section_entry_workspace.grid(row=50 , column=2)
    section_add_button.grid(row=50 , column=3)
    section_save_button.grid(row=51 , column=0)