import os
#File the list has been storing 
File="todolister.txt"
#display the content in the list
def display_list():
    #Check if the file exists
    if os.path.exists(File):
        with open(File,"r") as file: #Open the file to read current tasks
            task=file.read()
        if task.strip()=="":
            print("no task is there!")
        else:
            print(task+"\n")
    else:
        print("File not Found <xxx>")
#Adding the items in the tasks 
def add_list():
    tasks=[]
    print("Type the list one by one ,Type 'done' when you finished")
    while True:
        content=input("~>")
        if content.lower()=="done":
            print("*** Task updated successfully ***")
            break
        if content.strip():
            tasks.append(content.strip())
    #Giving the proper numbering list
    existing = []
    if os.path.exists(File):
        with open(File, "r") as f:
            existing = f.readlines()
    start_index = len(existing) + 1
    #Writing the tasks to the file
    with open(File, "a") as file:
        for index, task in enumerate(tasks, start=start_index):
            file.write(f"{index}. {task}\n")
        

def delete_item():
    if not os.path.exists(File):#Check the file exist or not
        print("File not Found <xxx>")
    
    with open(File, "r") as file:#Opening the file and Reading the file 
        tasks = file.readlines()
    
    if not tasks:#Check there is tasks in it 
        print("No tasks to delete!")
    
    print("Which task would you like to delete?")#Printing the list what to delete
    for i, task in enumerate(tasks, start=1):
        print(f"{task.strip()}")

    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            deleted_task = tasks.pop(choice - 1)#Removing the task
            with open(File, "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {deleted_task.strip()}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")
#main Function
def run():
    while True:
        print("-----TO-DO-LIST----")
        print("1.VIEW THE LIST")
        print("2.ADD THE ITEMS")
        print("3.DELETE THE ITEM")
        print("4.QUIT :)")
        value=input("ENTER THE OPTION :")
        if value=="1":
            display_list()  
        elif value=="2":
            add_list() 
        elif value=="3":
            delete_item()         
        elif value=="4":
            print("Thank You :)")
            break
    
if __name__ == "__main__":
    run()
