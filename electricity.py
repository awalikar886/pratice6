import sys

# If user provides 1 value: units consumed
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    units = float(sys.argv[1])
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    units = 100.0     # default units
    print("No input given — using default value:")

# Rate per unit
rate = 5

# Calculate bill
bill_amount = units * rate

# Print results
print("\n--- Electricity Bill Calculation ---")
print("Script Name:", script_name)
print("Units Consumed:", units)
print("Rate per Unit: ₹", rate)
print("Total Bill Amount: ₹", bill_amount)
