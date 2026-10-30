# Energy Conservation Before-and-After Analysis

appliances = ["Fan", "Light", "Air Conditioner", "Refrigerator", "TV"]

# Electricity usage in kWh before the intervention
before = [100, 80, 300, 150, 60]

# Electricity usage in kWh after the intervention
after = [70, 40, 210, 135, 45]

results = []

print("ENERGY CONSERVATION ANALYSIS")
print("-" * 55)

for i in range(len(appliances)):
    old_usage = before[i]
    new_usage = after[i]

    if old_usage <= 0 or new_usage < 0:
        print("Invalid data for", appliances[i])
        continue

    savings = old_usage - new_usage
    savings_percentage = (savings / old_usage) * 100

    results.append((
        appliances[i],
        old_usage,
        new_usage,
        savings,
        savings_percentage
    ))

    print("\nAppliance:", appliances[i])
    print("Before Usage:", old_usage, "kWh")
    print("After Usage:", new_usage, "kWh")
    print("Energy Saved:", savings, "kWh")
    print(f"Savings Percentage: {savings_percentage:.2f}%")

# Rank appliances by percentage savings
results.sort(key=lambda x: x[4], reverse=True)

print("\n" + "-" * 55)
print("APPLIANCE RANKING BY SAVINGS PERCENTAGE")
print("-" * 55)

for rank, item in enumerate(results, start=1):
    print(
        f"{rank}. {item[0]} - "
        f"{item[4]:.2f}% savings "
        f"({item[3]:.2f} kWh)"
    )

# Calculate overall energy savings
total_before = sum(before)
total_after = sum(after)
total_savings = total_before - total_after

print("\n" + "-" * 55)
print("OVERALL ENERGY SAVINGS")
print("Total Before:", total_before, "kWh")
print("Total After:", total_after, "kWh")
print("Total Energy Saved:", total_savings, "kWh")
print(f"Overall Savings: {total_savings / total_before * 100:.2f}%")
