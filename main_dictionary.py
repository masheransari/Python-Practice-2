# This file is for understanding about the Dictionaries in Python.
# Dictionary is just like a HashMap in Java Like

month = {
    "jan": "January",
    "feb": "Feburary",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "Jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "Novmber",
    "dec": "December"
}

print(month)
print(month['jan'])
# If by mistake we put un entered key just to find their value so we can use this funtion
print(month.get('JAN',"ERROR"))