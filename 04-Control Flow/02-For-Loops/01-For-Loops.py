# For Loops - is used to execute the same instruction over and over again, a specific number of times.
# range() - generates a series of integer numbers. The i variable is used to iterate over the numbers.
# The code that gets repeated in the for loop must be indented. Indentation- is the spaces at the beginning of lines.

#Define the number of iterations
for i in range(3):
  #Statement that gets repeated
  print("Hello") # => prints Hello 3x

for i in range(100):
  print("Hello") # => prints Hello 100x

for i in range(10):
  print(i) # => prints 0 - 9

for i in range(5):
    print("Congrats!") # => prints Congrats! 5x

for num in range(5):
print("Coding is fun!") # => prints error bcz-the code that gets repeated must be indented

for num in range(6)
  print(num) # => prints error bcz-missing colon : symbol