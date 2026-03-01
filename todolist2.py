import time
tasks = []
is_running = True
print("Welcome Hella 👑\n")
print("1. Add task\n"
      "2. View tasks\n"
      "3. Delete tasks\n"
      "4. Mark task complete\n"
      "5. Exit\n")
to_do = input("What would you like to do today?: ")

while is_running:
    if to_do == "1":
        print("\n-----ADD TASK-------")
        add_task = input("What task would you like to add?: ")
        tasks.append(add_task)
        print("Adding...")
        time.sleep(2)
        print("Task added!\n")
        print("1. Add task\n"
          "2. View tasks\n"
          "3. Delete tasks\n"
          "4. Mark task complete\n"
          "5. Exit\n")
        to_do = input("What would you like to do today?: ")
    elif to_do == "2":
        print("-----ALL TASKS-----")
        for task in tasks:
            print(task, end="\n")
        print()
        print("1. Add task\n"
              "2. View tasks\n"
              "3. Delete tasks\n"
              "4. Mark task complete\n"
              "5. Exit\n")
        to_do = input("What would you like to do today?: ")
    elif to_do == "3":
        print("-----DELETE TASK-----")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        if tasks:
            try:
                delete_index = int(input("Enter task number to delete: ")) - 1
                tasks.pop(delete_index)
                print("Deleting...")
                time.sleep(1)
                print("Task deleted!\n")
            except:
                print("Invalid index!\n")
        else:
            print("No tasks to delete!\n")

        print_menu = ("1. Add task\n"
                      "2. View tasks\n"
                      "3. Delete tasks\n"
                      "4. Mark task complete\n"
                      "5. Exit\n")
        print(print_menu)
        to_do = input("What would you like to do today?: ")

    elif to_do == "4":
        print("-----MARK TASK COMPLETE-----")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        if tasks:
            try:
                complete_index = int(input("Enter task number to mark complete: ")) - 1
                tasks[complete_index] = tasks[complete_index] + " ✅"
                print("Updating...")
                time.sleep(1)
                print("Task marked complete!\n")
            except:
                print("Invalid index!\n")
        else:
            print("No tasks available!\n")

        print("1. Add task\n"
              "2. View tasks\n"
              "3. Delete tasks\n"
              "4. Mark task complete\n"
              "5. Exit\n")
        to_do = input("What would you like to do today?: ")

    elif to_do == "5":
        print("Exiting program... Goodbye 👑")
        is_running = False

    else:
        print("Invalid option!\n")
        to_do = input("Choose a valid option: ")

