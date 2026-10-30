
# Environmental Monitoring Data Analyzer

# Each nested list contains readings for one day
# Example: Air quality readings (AQI)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

readings = [
    [45, 50, 55],
    [80, 90, 85],
    [120, 130, 125],
    [60, 65, 70],
    [160, 170, 180]
]

# AQI classification thresholds (illustrative)
good_limit = 50
moderate_limit = 100

all_readings = []

print("ENVIRONMENTAL MONITORING DATA ANALYZER")
print("=" * 45)

for i in range(len(readings)):
    daily_readings = readings[i]

    # Calculate daily average
    average = sum(daily_readings) / len(daily_readings)

    # Find minimum and maximum
    minimum = min(daily_readings)
    maximum = max(daily_readings)

    # Classify the observation
    if average <= good_limit:
        category = "Good"
    elif average <= moderate_limit:
        category = "Moderate"
    else:
        category = "Poor"

    print("\nDay:", days[i])
    print("Readings:", daily_readings)
    print(f"Average:", round(average, 2))
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Classification:", category)

    # Store readings for overall analysis
    all_readings.extend(daily_readings)

# Overall analysis
print("\n" + "=" * 45)
print("OVERALL ENVIRONMENTAL ANALYSIS")

overall_average = sum(all_readings) / len(all_readings)
lowest_reading = min(all_readings)
highest_reading = max(all_readings)

print(f"Overall Average: {overall_average:.2f}")
print("Lowest Reading:", lowest_reading)
print("Highest Reading:", highest_reading)

print("\nDays exceeding the moderate threshold:")

found = False

for i in range(len(readings)):
    average = sum(readings[i]) / len(readings[i])

    if average > moderate_limit:
        print(days[i], "- Average:", round(average, 2))
        found = True

if not found:
    print("No days exceeded the threshold.")
