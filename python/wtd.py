from tkinter import * 

root = Tk()
root.title("WTD")
root.geometry(f"600x600")

def add_section(app , monitor , workspace , section , window , n ):


    section.append([app.get() , monitor.get()  , workspace.get()])

    for x in section:
        Message(window , text=x[0] , width=100).grid(row = n , column=0)
        Message(window , text=x[1] , width=100).grid(row = n , column=1)
        Message(window , text=x[2] , width=100).grid(row = n , column=2)
        n+=1

    app.delete(0 , END)
    monitor.delete(0 , END)
    workspace.delete(0 , END)
    print(section)



def add_protocol():
    add_protocol_window = Toplevel(root)
    add_protocol_window.title("Second Window")

    section_list= [["c" , "c" , "c"],["c" , "c " , "c"]]
    n= len(section_list)
    protocol_name_mess = Message( add_protocol_window , text="Please enter the protocol name:"  , width=250)
    protocol_name_input = Entry( add_protocol_window  , borderwidth=2)

    section_app         = Message(add_protocol_window , text="App to run:" , width=100)
    section_monitor     = Message(add_protocol_window , text="monitor:" , width=100)
    section_workspace   = Message(add_protocol_window , text="workspace:" , width=100)
    
    #comment
    a = 10
    section_entry_app           =Entry(add_protocol_window , width=30 , borderwidth= 2)
    section_entry_monitor       =Entry(add_protocol_window , width=30 , borderwidth= 2)
    section_entry_workspace     =Entry(add_protocol_window , width=30 , borderwidth= 2)
    
    section_add_button          =Button(add_protocol_window , text="Add section" , command= lambda:
        add_section(section_entry_app , section_entry_monitor , section_entry_workspace , section_list , add_protocol_window , n))



    protocol_name_mess.grid(row=0 , column=0)
    protocol_name_input.grid(row=0 , column=1)


    
    section_app.grid(row=1 , column=0)
    section_monitor.grid(row=1 , column=1)
    section_workspace.grid(row=1 , column=2)


    for x in section_list:
        Message(add_protocol_window , text=x[0] , width=100).grid(row = n , column=0)
        Message(add_protocol_window , text=x[1] , width=100).grid(row = n , column=1)
        Message(add_protocol_window , text=x[2] , width=100).grid(row = n , column=2)
        n+=1
        print("done")
    n=2

    section_entry_app.grid(row=50 , column=0)
    section_entry_monitor.grid(row=50 , column=1)
    section_entry_workspace.grid(row=50 , column=2)
    section_add_button.grid(row=50 , column=3)



add_button = Button(root , text="add" , padx=10 , pady=10 , command= lambda: add_protocol())


add_button.grid(row=0 , column= 0)

root.mainloop()