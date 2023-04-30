# Selection is like a fork in the road. Selection allows your programs to decide which path to take
# Conditional statements, or if-else statements, allow programs to perform different actions based on the conditions met.

#sets the value of age
age = 22
if age >= 18:
  # executed only if customer is over-age
  print("Regular price") 
else:
  #executed only if age is less than 18
  print("Discount")

age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")

is_student = False
age = 16
print(is_student and (age < 18))

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")