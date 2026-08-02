# Nepali month names
bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
    "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
]

# Customer data
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]

# Function to convert date
def convert_date(date_str, from_cal, to_cal):
    year, month, day = map(int, date_str.split("-"))

    if from_cal == to_cal:
        return date_str

    if from_cal == "AD" and to_cal == "BS":
        year += 56
    elif from_cal == "BS" and to_cal == "AD":
        year -= 56

    return f"{year:04d}-{month:02d}-{day:02d}"

# Function to add ordinal suffix
def ordinal(day):
    if 10 <= day % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"

# Function to format date
def format_date(date_str, calendar, style):
    year, month, day = map(int, date_str.split("-"))

    if style == "iso":
        return f"{year:04d}-{month:02d}-{day:02d} {calendar}"

    elif style in ["full", "nepali"]:
        month_name = bs_months[month - 1]
        return f"{ordinal(day)} {month_name}, {year} {calendar}"

# Process all customers
for customer in customers:
    converted = convert_date(customer["date"], customer["cal"], customer["need"])
    formatted = format_date(converted, customer["need"], customer["style"])

    print(f"{customer['name']} | Original: {customer['date']} {customer['cal']} | Converted: {formatted}")