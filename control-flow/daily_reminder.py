Task = str(input("Enter your task: "))
Priority = str(input("Enter task's priority (high, medium, low): "))
Time_Bound = str(input("Is the task time bound? (yes, no): "))
message = "that requires immediate attention today!"

match priority:

    case "high":
        if time_bound == "yes":
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
print()