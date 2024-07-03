# Constants
MONTH_COUNT = 13
REST_DAYS = [8, 9, 15, 16, 17, 18]
LAST_WEEK_DAY = [17, 34]
DAY_COUNT = 51

# Function to generate the month text
def generate_month_text(month, days_in_month):
    week = 1
    day_of_week = 1
    txtoutput = f"  (WEEK {week})"
    month_text = [f"  MONTH {month:02d} {'#' * 60}"]

    for day in range(1, days_in_month + 1):
        sday = f"{day:02d}"

        if day_of_week in REST_DAYS:
            txtoutput += f" [{sday}]"
        else:
            txtoutput += f" {sday}"

        if day in LAST_WEEK_DAY:
            month_text.append(txtoutput)
            week += 1
            day_of_week = 1
            txtoutput = f"  (WEEK {week})"
        else:
            day_of_week += 1

    month_text.append(txtoutput)
    return month_text

# Function to print the Martian calendar
def print_martian_calendar():
    odd_months = []
    even_months = []

    for month in range(1, MONTH_COUNT + 1):
        days_in_month = DAY_COUNT
        if month == 13:
            days_in_month += 1

        month_text = generate_month_text(month, days_in_month)
        if month % 2 == 1:
            odd_months.append(month_text)
        else:
            even_months.append(month_text)

    # Combine and print odd and even months line by line
    for i in range(len(odd_months)):
        odd = odd_months[i]
        even = even_months[i] if i < len(even_months) else [""] * len(odd)

        max_lines = max(len(odd), len(even))
        for j in range(max_lines):
            odd_line = odd[j] if j < len(odd) else ""
            even_line = even[j] if j < len(even) else ""
            print(f"{odd_line:<60} {even_line}")


print_martian_calendar()
