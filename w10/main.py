# Creates a mileage tracker for running.

# Starting inputs
days = input("What day would you like to start with? ")
miles = input("How many miles did you run on {days}? ")

# A list of dictionaries with day and miles that the functions will pull from.
tracker = {
    "Day": days,
    "Miles": miles
}


# This adds new miles to the dictionary list.


def new_mileage(tracker):
    program_continue = True
    while program_continue:
        next_value = input("would you like to continue? Type y for yes or"
                           " n for no. ").lower())
        if next_value == "n":
            return False
        days = input("What's the next day? ")
        miles = float(input(f"How many miles did you run on {days}? "))
        new_mile == []
        new_mile["Day"] = days
        new_mile["Miles"] = miles
        tracker.append(new_mile)


new_mileage()

# function gives the total miles.


def add(tracker):
    total = sum(item['Miles'])
    return f"Your total mileage is: {total} miles."

# function creates an average based off total miles/ the length of the
# dictionary.


def average(tracker):
    average = sum(item['Miles'] for item in tracker) / len(tracker)
    return f"Your average was {average} miles per day."

# gives user the output based on the inputs provided for each function.


print(add(tracker))
print(average(tracker))
