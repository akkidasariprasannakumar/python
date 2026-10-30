
# Weekly Electricity Consumption Matrix

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

appliances = ["Fan", "Light", "Refrigerator", "TV"]

# Daily electricity consumption in kWh
consumption = [
    [2, 1, 3, 2, 2, 3, 2],   # Fan
    [1, 1, 1, 1, 1, 2, 2],   # Light
    [3, 3, 3, 3, 3, 3, 3],   # Refrigerator
    [2, 2, 1, 2, 2, 3, 2]    # TV
]

# Weekly limits for each appliance (kWh)
limits = [18, 10, 22, 16]

# Calculate appliance totals
print("WEEKLY ELECTRICITY CONSUMPTION")
print("-" * 60)

appliance_totals = []

for i in range(len(appliances)):
    total = sum(consumption[i])
    appliance_totals.append(total)

    print(f"{appliances[i]}: {total} kWh")

    if total > limits[i]:
        print("WARNING: Weekly consumption limit exceeded!")

# Calculate daily totals
print("\nDAILY ELECTRICITY TOTALS")
print("-" * 60)

daily_totals = []

for j in range(7):
    total = 0

    for i in range(len(appliances)):
        total += consumption[i][j]

    daily_totals.append(total)
    print(f"{days[j]}: {total} kWh")

# Identify days exceeding the daily limit
daily_limit = 10

print("\nDAILY LIMIT CHECK")
for j in range(7):
    if daily_totals[j] > daily_limit:
        print(f"Warning: {days[j]} exceeded {daily_limit} kWh")

# Overall weekly consumption
weekly_total = sum(appliance_totals)

print("\nTotal weekly consumption:", weekly_total, "kWh")

