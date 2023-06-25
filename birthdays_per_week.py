from datetime import datetime, timedelta

users = [
    {"name": "Ed", "birthday": datetime(1995, 4, 26)},
    {"name": "Dan", "birthday": "27.04.1995"},
    {"name": "Carl", "birthday": datetime(1993, 7, 4)},
]


def get_week() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_week = current_date + timedelta(days=5 - current_date.weekday())
    return start_week.date(), (start_week + timedelta(6)).date()


def get_birthdays_per_week(users=list):
    current_year = datetime.now().year

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        if not isinstance(birthday, datetime):
            birthday = datetime.strptime(birthday, "%d.%m.%Y")
        old = current_year - birthday.year
        birthday_weekday = birthday.strftime("%A %d %B")
        birthday = birthday.replace(year=current_year).date()
        start, end = get_week()
        if start <= birthday <= end:
            print(f"{name} will celebrate {old}`th at {birthday_weekday}!")


if __name__ == "__main__":
    get_birthdays_per_week(users)
