# Lists are used to store items. 
# We can create a list by using square brackets with commas separating items. Like this:
# If you want to access a certain item in the list, you can do this by using its index in square brackets.
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2]) 

# Lists can hold different data types, such as strings and numbers.
x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])

# we can use nested lists to represent 2D grids, such as matrices
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

# To access the elements of a matrix, we specify the row and the column of the item using square brackets:
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2]) # => 6

# Strings can be indexed like lists too!
str = "Hello world!"
print(str[6]) # => w