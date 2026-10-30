# Food Waste Monitoring System

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

meals_prepared = [100, 120, 150, 110, 130]
meals_served = [90, 100, 120, 95, 100]

# Acceptable food wastage percentage
waste_limit = 15

print("FOOD WASTE MONITORING SYSTEM")
print("-" * 55)

total_prepared = 0
total_served = 0
total_leftovers = 0

for i in range(len(days)):
    prepared = meals_prepared[i]
    served = meals_served[i]

    leftovers = prepared - served

    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid data for", days[i])
        continue

    waste_percentage = (leftovers / prepared) * 100

    total_prepared += prepared
    total_served += served
    total_leftovers += leftovers

    print("\nDay:", days[i])
    print("Meals Prepared:", prepared)
    print("Meals Served:", served)
    print("Leftovers:", leftovers)
    print(f"Wastage Percentage: {waste_percentage:.2f}%")

    if waste_percentage > waste_limit:
        print("Status: WASTE LIMIT EXCEEDED")
    else:
        print("Status: ACCEPTABLE")

# Calculate overall wastage
print("\n" + "-" * 55)
print("WEEKLY SUMMARY")
print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftovers:", total_leftovers)

if total_prepared > 0:
    overall_waste = (total_leftovers / total_prepared) * 100
    print(f"Overall Wastage: {overall_waste:.2f}%")

    if overall_waste > waste_limit:
        print("Overall Status: WASTE LIMIT EXCEEDED")
    else:
        print("Overall Status: ACCEPTABLE")
