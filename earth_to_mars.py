from datetime import datetime, timedelta

# Define constants
SOL_IN_EARTH_DAYS = 1.027491252
DAYS_IN_MARTIAN_YEAR = 664
DAYS_IN_MONTH = 51
EXTRA_DAY_IN_LAST_MONTH = 1

def earth_to_martian_calendar(landing_date, query_date):
    # Calculate the difference in Earth days
    difference_in_days = (query_date - landing_date).days

    # Convert Earth days to Martian sols
    difference_in_sols = difference_in_days / SOL_IN_EARTH_DAYS
    print(difference_in_sols)
    print(f"Difference in sols:  {difference_in_sols}")

    # Determine the Martian year and day
    martian_year = int(difference_in_sols // DAYS_IN_MARTIAN_YEAR)
    remaining_sols = difference_in_sols % DAYS_IN_MARTIAN_YEAR


    # If remaining sols is negative, adjust the year and remaining sols
    if remaining_sols < 0:
        martian_year -= 1
        remaining_sols += DAYS_IN_MARTIAN_YEAR

    print(f"Remaining sols:  {remaining_sols}")

    # Determine the Martian month and day
    if remaining_sols >= (DAYS_IN_MONTH * 13) + EXTRA_DAY_IN_LAST_MONTH:
        martian_month = 13
        martian_day = int(remaining_sols - DAYS_IN_MONTH * 12)
    else:
        martian_month = int(remaining_sols // DAYS_IN_MONTH) + 1
        martian_day = int(remaining_sols % DAYS_IN_MONTH) + 1

    if martian_month == 14:
        martian_month = 13
        martian_day = 52

    if martian_year >= 0:
        martian_year += 1

    return martian_year, martian_month, martian_day

def main():
    # Request the user to input two dates
    landing_date_str = input("Enter the landing date on Mars (DD/MM/YYYY): ")
    query_date_str = input("Enter the query date on Earth (DD/MM/YYYY): ")

    # Convert input strings to datetime objects
    landing_date = datetime.strptime(landing_date_str, "%d/%m/%Y")
    query_date = datetime.strptime(query_date_str, "%d/%m/%Y")

    # Get the Martian date
    martian_year, martian_month, martian_day = earth_to_martian_calendar(landing_date, query_date)

    if martian_day < 10:
        smartian_day = "0"+str(martian_day)
    else:
        smartian_day = str(martian_day)


    if martian_month < 10:
        smartian_month = "0"+str(martian_month)
    else:
        smartian_month = str(martian_month)


    # Display the result
    print("Martian Date (DD/MM/Y*):"+smartian_day+"/"+smartian_month+"/"+str(martian_year))

if __name__ == "__main__":
    main()
