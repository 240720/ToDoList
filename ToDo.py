import tkinter
from tkinter import *

root=Tk()
root.title('TO-DO-LIST')
root.geometry('1000x650+400+250')
root.resizable(False,False)

task_list=[]

def addTask():
    task=text.get('1.0',END).strip()
    text.delete('1.0', END)

    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append({'task': task, 'completed': False})
        listbox.insert(END, task)

def removeTask():
    selection=listbox.curselection()
    if selection:
        task=listbox.get(selection[0])
        task_list.pop(selection[0])
        listbox.delete(selection[0])
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(f"{task['task']}\n")

def updateTask():
    selection = listbox.curselection()
    if selection:
        task = listbox.get(selection[0])
        updated_task = text.get('1.0', END).strip()
        text.delete('1.0', END)

        if updated_task:
            task_list[selection[0]]['task'] = updated_task
            listbox.delete(selection[0])
            listbox.insert(selection[0], updated_task)
            with open('tasklist.txt', 'w') as taskfile:
                for task in task_list:
                    taskfile.write(f"{task['task']}\n")

def markAsCompleted():
    selection = listbox.curselection()
    if selection:
        task_list[selection[0]]['completed'] = True
        listbox.itemconfig(selection[0], fg='red')
 
def openTaskFile():
    try:
        with open('tasklist.txt','r') as taskfile:
            tasks=taskfile.readlines()
    
        for task in tasks:
            if task!='\n':
                task = task.strip()
                task_list.append({'task': task, 'completed': False})
                listbox.insert(END, task)
    
    except:
        with open('tasklist.txt','w') as taskfile:
            pass


label=Label(root, text='MY DAY PLAN', font='ariel, 30 bold', width=5, bd=10, bg='#367588' ,fg='#f8f8ff')
label.pack(side='top',fill=BOTH)

text=Text(root, bd=2,height=2,width=70,font='ariel 12 bold')
text.place(x=270,y=130) 
text.focus()

button=Button(root, text='ADD' ,font='ariel, 11 bold' ,width=10,bd=4,bg='#007474',fg='white',command=addTask)
button.place(x=60,y=210)

button1=Button(root,text='REMOVE',font='ariel, 11 bold',width=10,bd=4,bg='#007474',fg='white',command=removeTask)
button1.place(x=60,y=280)

button2 = Button(root, text='UPDATE',font='ariel, 11 bold' ,width=10,bd=4,bg='#007474',fg='white', command=updateTask)
button2.place(x=60,y=350)

button3 = Button(root, text='MARK AS COMPLETED', font='ariel, 11 bold', width=18, bd=4, bg='#007474', fg='white', command=markAsCompleted)
button3.place(x=60, y=420)

listbox=Listbox(root,height=20,width=70,bd=5,font='ariel 12 bold',cursor='hand2' ,selectbackground='#5a95ff')
listbox.place(x=270,y=210)



openTaskFile()

root.mainloop()
