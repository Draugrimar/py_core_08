from datetime import datetime, timedelta

users = [
    {"name": "Ed", "birthday": datetime(1995, 4, 26)},
    {"name": "Dan", "birthday": "27.04.1995"},
    {"name": "Carl", "birthday": datetime(1993, 7, 4)},
    {"name": "Carl2", "birthday": datetime(1993, 7, 4)},
    {"name": "John", "birthday": "05.07.1995"}
]

def get_week() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_week = current_date + timedelta(days=5 - current_date.weekday())
    return start_week.date(), (start_week + timedelta(6)).date()

def parcer(birthdays):
    weekdays = {}
    for person in birthdays:
        weekday = datetime.strftime(person["birthday"], "%A")
        if weekday in weekdays:
            weekdays[weekday].append(person["name"])
        else:
            weekdays.update({weekday: [person["name"]]})
    

    for day, names in weekdays.items():
        print(f"{day}:", *names)


def get_birthdays_per_week(users=list):
    current_year = datetime.now().year
    birthdays = []
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        if not isinstance(birthday, datetime):
            birthday = datetime.strptime(birthday, "%d.%m.%Y")
        birthday = birthday.replace(year=current_year).date()
        start, end = get_week()
        if start <= birthday <= end:
            birthdays.append({"name": name, "birthday": birthday})

    parcer(birthdays)





if __name__ == "__main__":
    get_birthdays_per_week(users)
