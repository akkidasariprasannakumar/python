
# Campus Festival Registration and Financial Audit

# Participant list: (Registration ID, Name, Fee Paid)
participants = [
    ("R101", "Ravi", 500),
    ("R102", "Priya", 500),
    ("R103", "Arun", 500),
    ("R102", "Priya", 500),  # Duplicate registration
    ("R104", "Sita", 500)
]

# Sponsorship contributions: (Sponsor Name, Amount)
sponsors = [
    ("ABC Company", 10000),
    ("XYZ Company", 15000),
    ("College Management", 20000)
]

# Festival expenses: (Expense Name, Amount)
expenses = [
    ("Stage Decoration", 8000),
    ("Food", 12000),
    ("Sound System", 5000),
    ("Certificates", 2000)
]

registration_fee = 500

# Detect duplicate registrations
seen_ids = set()
unique_participants = []
duplicates = []

for participant in participants:
    reg_id, name, fee_paid = participant

    if reg_id in seen_ids:
        duplicates.append(participant)
    else:
        seen_ids.add(reg_id)
        unique_participants.append(participant)

# Registration audit
print("CAMPUS FESTIVAL FINANCIAL AUDIT")
print("=" * 45)

print("\n1. REGISTRATION DETAILS")
print("Total registration records:", len(participants))
print("Unique participants:", len(unique_participants))
print("Duplicate registrations:", len(duplicates))

for duplicate in duplicates:
    print("Duplicate:", duplicate[0], "-", duplicate[1])

# Calculate registration revenue
total_fees = sum(p[2] for p in unique_participants)
expected_fees = len(unique_participants) * registration_fee

print("\nRegistration fees collected:", total_fees)
print("Expected registration fees:", expected_fees)

if total_fees == expected_fees:
    print("Registration fee status: RECONCILED")
else:
    print("Registration fee status: MISMATCH")

# Sponsorship audit
print("\n2. SPONSORSHIP CONTRIBUTIONS")
total_sponsorship = 0

for sponsor in sponsors:
    print(sponsor[0], ": Rs.", sponsor[1])
    total_sponsorship += sponsor[1]

print("Total sponsorship: Rs.", total_sponsorship)

# Expense audit
print("\n3. FESTIVAL EXPENSES")
total_expenses = 0

for expense in expenses:
    print(expense[0], ": Rs.", expense[1])
    total_expenses += expense[1]

print("Total expenses: Rs.", total_expenses)

# Final financial balance
total_income = total_fees + total_sponsorship
balance = total_income - total_expenses

print("\n4. FINAL FINANCIAL SUMMARY")
print("Total registration income: Rs.", total_fees)
print("Total sponsorship income: Rs.", total_sponsorship)
print("Total income: Rs.", total_income)
print("Total expenses: Rs.", total_expenses)
print("Final balance: Rs.", balance)

if balance > 0:
    print("Status: SURPLUS")
elif balance < 0:
    print("Status: DEFICIT")
else:
    print("Status: BALANCED")
