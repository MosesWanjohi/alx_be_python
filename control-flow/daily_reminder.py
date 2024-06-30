task = str(input("Enter your task: "))
priority = str(input("Enter task's Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

#message = "that requires immediate attention today!"

match priority:

    case "high":
        if time_bound == "yes":
            message = "that requires immediate attention today!"
            print(task,  "is a", priority, "priority task", message)
        else:
            print(task,  "is a", priority, "priority task.", "Consider completing it when you have free time")

    case "medium":
        if time_bound == "yes":
            message = "that requires moderate attention today!"
            print(task,  "is a", priority, "priority task", message)
        else:
            print(task,  "is a", priority, "priority task.", "Consider completing it when you have free time")

    case "low":
        if time_bound == "yes":
            message = "that requires less attention today!"
            print(task,  "is a", priority, "priority task", message)
        else:
            print(task,  "is a", priority, "priority task.", "Consider completing it when you have free time")
    case _:
        print("Invalid priority input. Please enter high, medium, or low.")
