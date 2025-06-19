#Mini-Project
#To Do List

def addTask():
    newTask=input("Enter your new task to be added: ")
    ToDoList.append(newTask)
    print(ToDoList)

def rmvTask():
    task=input("Enter your task to be removed: ")
    ToDoList.remove(task)
    print(ToDoList)    

def markTask():
    task=input("Enter your task to be marked as completed: ")

    if task in ToDoList:
        ToDoList.remove(task)
        ToDoList.append(f"{task} ✅")
        print(ToDoList)
ToDoList=[]
while True:
    print("1. Add task\n2. Remove task\n3. Mark task as completed.")
    choice=int(input("Enter your choice: "))

    if choice ==1:
        addTask()
    elif choice ==2:
        rmvTask()
    elif choice ==3:
        markTask()
    else:
        print("Invalid input!")

