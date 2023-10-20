import customtkinter
import tkinter.messagebox
import pickle


root = customtkinter.CTk()
root.title("To-Do List")
root.config(bg="#09112e")

font1 = ("Arial", 18, "bold")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def completed_task():
    try:
        marked = listbox_tasks.curselection()
        temp = marked[0]
        temp_marked = listbox_tasks.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_tasks.delete(temp)
        listbox_tasks.insert(temp, temp_marked)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())

    pickle.dump(tasks, open("tasks.dat", "wb"))


frame_tasks = customtkinter.CTkFrame(master=root, width=5, height=5, corner_radius=5)
frame_tasks.pack()


listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.Y)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = customtkinter.CTkEntry(root, text_color="#050505", fg_color="#fff", width=280)
entry_task.pack()

button_add_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Add task", fg_color="#66cd00", hover_color="#458b00", bg_color="#09112e", cursor="hand2", width=48, command=add_task)
button_add_task.pack()

button_completed_task= customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Mark as completed ", fg_color="#0000ff" , hover_color="#0000cd", bg_color="#09112e", cursor="hand2", width=48, command=completed_task)
button_completed_task.pack()

button_delete_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Delete task", fg_color="#ff4040", hover_color="#8b2323", bg_color="#09112e", cursor="hand2", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = customtkinter.CTkButton(root, font=font1, text_color="#050505", text="Load task", fg_color="#9bcd9b", hover_color="#698b69", width=48, command=load_tasks)
button_load_task.pack()

button_save_task = customtkinter.CTkButton(root, font=font1, text_color="#050505", text="Save task", fg_color="#eee8cd", hover_color="#a9a9a9", width=48, command=save_tasks)
button_save_task.pack()

root.mainloop()
