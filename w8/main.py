# Creates a mileage tracker for running.

# inputs

days = input("What day would you like to start with? ")
miles = float(input(f"How many miles did you run on {days}? "))

tracker = [{
    "Day": days,
    "Miles": miles
},
]


def new_mileage(tracker):
    program_continue = True
    while program_continue:
        next_value = input("would you like to continue? Type y for yes or"
                           " n for no. ").lower()
        if next_value == "n":
            return False
        days = input("What's the next day? ")
        miles = float(input(f"How many miles did you run on {days}? "))
        new_mileage = {}
        new_mileage["Day"] = days
        new_mileage["Miles"] = miles
        tracker.append(new_mileage)


new_mileage(tracker)


def add(tracker):
    total = sum(item['Miles'] for item in tracker)
    return f"Your total mileage is: {total} miles."


def average(tracker):
    average = sum(item['Miles'] for item in tracker) / len(tracker)
    return f"Your average was {average} miles per day."


print(add(tracker))
print(average(tracker))
