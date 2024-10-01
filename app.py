def task():
    tasks = []
    print("----- Welcom TO The Task Manager APP -----")

    total_task = int(input(" Enter How Many Task You Want To Add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter Your Task Name {i} = ")
        tasks.append(task_name)

    print(f"Todoy's Tasks Are\n{tasks}")

    while True:
        operation = int(input(f"1-Add\n2-Update\n3-Delete \n4-View \n5-Exit \n"))
        if operation == 1:
            add = input("Enter Your Tasks Name = ")
            tasks.append(add)
            print(f"Task {add} Has Been Successfully Added...")

        elif operation == 2:
            updated_val = input("Enter The Task Name You Want To Updated = ")
            if updated_val in tasks:
                up = input("Enter New Task =")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated Task {up}")

        elif operation == 3:
            del_val = input("Which Task You Want To Deleted = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} Has Been deleted...")

        elif operation == 4:
            print(f"Totak Tasks = {tasks}")

        elif operation == 5:
            print("Closing The Task Porgram....")
            break

        else:
            print("Invalid Input")


task()                       