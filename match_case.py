# Match case also known as switch, execute some code if value matches a case

day = 1

def day_of_week(day):
    if day == 1:
        return "Monday"
    elif day ==2:
        return "Tuesday"
    elif day ==3:
        return "Wednesday"
    elif day ==4:
        return "Thursday"
    elif day ==5:
        return "Friday"
    elif day ==6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid input"

def day_of_the_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid input"


print(day_of_the_week(5))

def is_weekend(day):
    match day:
        case "Sunday" | "Sunday":
            return "Weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case _:
            return "Not a day"

print(is_weekend("Sunday"))