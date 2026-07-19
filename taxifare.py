trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for i, trip in enumerate(trips, start=1):
    distance = trip["distance"]
    hour = trip["hour"]

    # Calculate fare
    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + (distance - 2) * 35
    else:
        fare = 150 + (8 * 35) + (distance - 10) * 28

    # Apply night surcharge (10 PM to 5 AM)
    if hour >= 22 or hour < 5:
        fare = fare * 1.10

    print(f"Trip {i}")
    print(f"Distance: {distance} km")
    print(f"Hour: {hour}:00")
    print(f"Taxi Fare: NPR {fare:.2f}")
    print("-" * 30)