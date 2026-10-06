# To-Do List
# Build a simple program that allows users to:
#  Add tasks
# View tasks
# Mark tasks as completed
# Delete tasks
ToDo_list = {}
menu = ""
while menu !="5":
    menu = input("Select 1-4 for menu: \n1.Add task\n2.View All Tasks\n3.Mark task as completed\n4.Delete Task\n5.Exit\nEnter an option:")
    if menu == "1":
        print("you've choosen : ",menu  )
    # for task in ToDo_list:
        task = input("Add a task to your ToDo list: ").title()
    # status = input ("Enter status : Pending or completed: ")
        ToDo_list[task] = "pending"
        print("Task added")
    elif menu =="2":
        for task, status in ToDo_list.items():
            print(f"{task}:{status} ")
    elif menu =="3":
        Completed_task = input("Enter a task you'd like to mark as complete: ").title()
        if Completed_task in ToDo_list:
            ToDo_list[Completed_task] = "completed"
            print(f"{Completed_task}:{ToDo_list[Completed_task]}")
        else:
            print("Task not found")
    elif menu == "4":
        delete_task = input("Enter a task you'd like to delete ").title()
        if delete_task in ToDo_list:
            del ToDo_list[delete_task]
            print(f"{delete_task} removed successfully")
    elif menu =="5":
        print("Exiting program")
        exit() 
    else:
        print("Invalid selection")
        print("Try again")