from datetime import datetime
from calendar import monthrange

def calculate_age():
    # Get the user's date of birth
    dob_input = input("Enter your date of birth (MM-DD-YYYY): ")
    try:
        dob = datetime.strptime(dob_input, "%m-%d-%Y")
    except ValueError:
        print("Invalid date format. Please use MM-DD-YYYY.")
        return

    # Get the current date
    today = datetime.today()

    # Calculate the difference in years, months, and days
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Adjust for negative days
    if days < 0:
        # Get the number of days in the previous month
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days_in_prev_month = monthrange(prev_year, prev_month)[1]

        days += days_in_prev_month
        months -= 1

    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12

    # Display the result
    print(f"You are {years} years, {months} months, and {days} days old.")

# Run the function
calculate_age()
