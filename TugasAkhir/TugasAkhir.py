import tkinter
import random
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from datetime import datetime
from userService import userService

# Modul 1
# Modul 2
# Modul 3
# Modul 4
# Modul 5
# Modul 8

class ToDoListApp(tkinter.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tkinter.Tk.__init__(self, *args, **kwargs)
        
        container = tkinter.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        
        self.frames = {} 
    
        for F in (login, mainMenu):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(login)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#login

class login(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        
        
        def on_click():
            email = text_input_email.get()
            password = text_input_Password.get()
            logininfo = userService(email, password)
            if logininfo.login():
                controller.show_frame(mainMenu)
            else:
                messagebox.showwarning('Caution!', 'Wrong Email or Password',)
        
        self.config(bg= "white")        
         
        button_submit = tkinter.Button(
            self, text = "Login", width= 25, command = on_click, 
            state = ACTIVE, bg= "white").place(x = 180, y = 200) 
        
        label_email = tkinter.Label(
            self, text = "Email:", bg= "white").place(x=50, y=80)

        label_password = tkinter.Label(
            self, text = "Password:", bg= "white").place(x=50, y=120)
        

        text_input_email = tkinter.Entry(self, width=50)
        text_input_email.place(x=120, y=80)
        
        text_input_Password = tkinter.Entry(self, width=50)
        text_input_Password.place(x=120, y=120)
        


#mainMenu

class mainMenu(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        
        def update_tasks():
            clear_listbox()
            for task in tasks:
                lb_tasks.insert("end", task)
            numtask = len(tasks)
            label_dsp_count['text'] = numtask


        def update_history():
            lb_history.delete(0, "end")
            for i in history:
                lb_history.insert("end", i)


        def clear_listbox():
            lb_tasks.delete(0, "end")


        def add_task():
            Ntask = text_input_task.get()
            if Ntask != "Add Text...":
                tasks.append(Ntask)
                update_tasks()
            else:
                messagebox.showwarning('Caution!', 'Please add a task',)
            text_input_task.delete(0, 'end')


        def delete_all():
            conf = messagebox.askquestion(
                'Caution!', 'Delete Tasks?')
            print(conf)
            if conf.upper() == "YES":
                global tasks
                tasks = []
                update_tasks()
            else:
                pass


        def delete_one():
            de = lb_tasks.get("active")
            if de in tasks:
                tasks.remove(de)
                history_text = "done " + de + " at " + time()
                history.append(history_text)
            update_tasks()
            update_history()


        def sort_asc():
            tasks.sort()
            update_tasks()


        def sort_dsc():
            tasks.sort(reverse=True)
            update_tasks()


        def random_task():
            update_tasks()
            random_index = random.randint(0,len(tasks)-1)
            lb_tasks.itemconfig(random_index, {'bg':'blue'})
            lb_tasks.activate(random_index)


        def save_act():
            savecon = messagebox.askquestion(
                'Save Confirmation', 'Save your progress?')
            if savecon.upper() == "YES":
                with open("SaveFile.txt", "w") as filehandle1:
                    for listitem1 in tasks:
                        filehandle1.write('%s\n' % listitem1)
                with open("History.txt", "w") as filehandle2:
                    for listitem2 in history:
                        filehandle2.write('%s\n' % listitem2)        
            else:
                pass


        def load_act():
            loadcon = messagebox.askquestion(
                'Konfirmasi Save', 'Load your progress?')
            if loadcon.upper() == "YES":
                tasks.clear()
                history.clear()
                with open('SaveFile.txt', 'r') as filereader1:
                    for line1 in filereader1:
                        currentask = line1
                        tasks.append(currentask)
                    update_tasks()
                with open('History.txt', 'r') as filereader2:
                    for line2 in filereader2:
                        currenthistory = line2
                        history.append(currenthistory)
                    update_history()

            else:
                pass


        def exit_app():
            confex = messagebox.askquestion(
                'Quit Confirmation', 'Are you sure you want to quit?')
            if confex.upper() == "YES":
                self.destroy()
            else:
                pass


        def time():
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S %B %d %Y")
            return current_time


        def on_entry_click(event):
            if text_input_task.get() == 'Add Text...':
                text_input_task.delete(0, "end") 
                text_input_task.insert(0, '') 
                text_input_task.config(fg = 'black')
                
                
        def on_focus_out(event):
            if text_input_task.get() == '':
                text_input_task.insert(0, 'Add Text...')
                text_input_task.config(fg = 'grey')
        
        self.config(bg= "white")
        
        tasks = []
        history = []
        
        
        label_title = tkinter.Label(self, bg= "white", text="To Do List")
        label_title.grid(row=0, column=0)

        label_blank = tkinter.Label(self, bg= "white", text="")
        label_blank.grid(row=8, column=0)

        label_task_dsply = tkinter.Label(self, bg= "white", text="Task")
        label_task_dsply.grid(row=1, column=1)

        label_history_dsply = tkinter.Label(self, bg= "white", text="History")
        label_history_dsply.grid(row=1, column=2)

        label_dsp_count = tkinter.Label(self, bg= "white", text="")
        label_dsp_count.grid(row=0, column=3)

        label_dsp_task = tkinter.Label(self, bg= "white", text="")
        label_dsp_task.grid(row=0, column=1)

        text_input_task = tkinter.Entry(self, width=15)
        text_input_task.grid(row=2, column=1)
        text_input_task.insert(0, "Add Text...")
        text_input_task.bind('<FocusIn>', on_entry_click)
        text_input_task.bind('<FocusOut>', on_focus_out)
        text_input_task.config(fg = 'grey')

        text_add_bttn = tkinter.Button(
            self, text="Add Task", fg="green", width=15, bg= "white", command=add_task)
        text_add_bttn.grid(row=1, column=0)

        done_bttn = tkinter.Button(
            self, text="Done Task", width=15, bg= "white", command=delete_one)
        done_bttn.grid(row=2, column=0)

        delall_bttn = tkinter.Button(
            self, text="Delete all", width=15, bg= "white", command=delete_all)
        delall_bttn.grid(row=3, column=0)

        sort_asc = tkinter.Button(
            self, text="Sort (ASC)", width=15, bg= "white", command=sort_asc)
        sort_asc.grid(row=4, column=0)

        sort_dsc = tkinter.Button(
            self, text="Sort (DSC)", width=15, bg= "white", command=sort_dsc)
        sort_dsc.grid(row=5, column=0)

        random_bttn = tkinter.Button(
            self, text="Random Task", width=15, bg= "white", command=random_task)
        random_bttn.grid(row=6, column=0)

        exit_bttn = tkinter.Button(
            self, text="Exit app", width=15, bg= "white", command=exit_app)
        exit_bttn.grid(row=7, column=0)

        save_button = tkinter.Button(
            self, text="Save Task", width=15, bg= "white", command=save_act)
        save_button.grid(row=10, column=1)

        load_button = tkinter.Button(
            self, text="Load Task", width=15, bg= "white", command=load_act)
        load_button.grid(row=10, column=0)

        lb_tasks = tkinter.Listbox(
            self)
        lb_tasks.grid(row=3, column=1, rowspan=7, columnspan=1)

        lb_history = tkinter.Listbox(
            self, width=50)
        lb_history.grid(row=3, column=2, rowspan=7, columnspan=1)


# main loop
ToDoListApp().mainloop()
