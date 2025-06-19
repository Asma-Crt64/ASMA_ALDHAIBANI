from datetime import datetime, date


today = date.today()
print("Today's date:", today)


print("Day of week:", today.strftime("%A"))


new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print("Days until New Year:", days_left)
