# Room rates
standard_rate = 100
deluxe_rate = 150
suite_rate = 250

# Input values
room_type = 'Deluxe'
nights = 5
season = 'peak'
loyalty_member = True

# Base cost calculation
if room_type == 'Standard':
    base_cost = standard_rate * nights
elif room_type == 'Deluxe':
    base_cost = deluxe_rate * nights
elif room_type == 'Suite':
    base_cost = suite_rate * nights
else:
    base_cost = 0
    print("Invalid room type")

# Length of stay discount
if nights > 7:
    discount = 0.20
elif nights > 3:
    discount = 0.10
else:
    discount = 0.0
base_cost = base_cost - (base_cost * discount)

# Season adjustment
if season == 'peak':
    base_cost = base_cost + (base_cost * 0.20)
elif season == 'off':
    base_cost = base_cost - (base_cost * 0.15)

# Loyalty member discount
if loyalty_member:
    base_cost = base_cost - (base_cost * 0.05)

# Output the final cost
print(f"The final booking cost is: ${base_cost:.2f}")
