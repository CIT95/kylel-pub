# My Code
age = input("What is your current age?")
# Convert age into integer
age_int = int(age)
# Assign variables for days, weeks, months
days = 365
weeks = 52
months = 12
# Assign variables for calculating the days, weeks,
# and months left
days_left = (90 * days) - (age_int * days)
weeks_left = (90 * weeks) - (age_int * weeks)
months_left = (90 * months) - (age_int * months)
# create the calculations for calendar year
calendar_year_90 = (2022-age_int) + 90
print(calendar_year_90)
# Print the final calculation
print(f"You have {days_left} days, {weeks_left} weeks,"
      f"and {months_left} months left.")
print(f"You will be 90 years old in {calendar_year_90}.")
