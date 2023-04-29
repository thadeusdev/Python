# Python
<img src="./images/python.jpg" />

## Hello world
```
print("Hello world)
```

## Simple Operations
```
print(2 + 2)
print(5 + 4 - 3)
print(10 / 2)
print(2 * (3 + 4))
```
- Using a single slash to divide numbers produces a decimal (or float, as it’s known in programming)

## Quotient & Remainder
### Quotient
#### floor division
- ``Quotient`` just means the quantity produced by the division of two numbers.
- ``Floor division`` is done using two forward slashes and is used to determine the ``quotient`` of a division.
```
print(20 // 6) # => 3
```

### Remainder
#### modulo operator
- ``modulo operator``–which is carried out with a percent symbol (%)–to get the remainder of a given division.
```
print(20 % 6) # => 2
print(1.25 % 0.5) # => 0.25
```
## Strings
- We can create a string by entering text between two single or double quotation marks. Like this:
```
print("python is fun!")
print('always look on the bright side of life')
print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
```
- The delimiter ``(" or ')`` used for a string doesn't affect how it behaves in any way.

### Newlines
- To create a new line we use \n.
```
print("One \nTwo \nThree")
```
- Based on what we just learned, can you guess how we represent tab? That’s right, it’s ``\t``.
- ``\n`` is useful, but it can be a bit of a pain if we’re trying to format lots of multiline text.

- There’s another way though! Newlines are automatically added for strings created using ``three quotes``.
For example:

```
print("""This
is a
multiline
text""")
```

### String Operations
### concatenation
```
print("Spam" + "eggs") # => Spameggs
print("2" + "2") # => 22
```

- Multiplying a ``string`` by an ``integer``, produces a repeated version of the original string. Like this:
```
print("spam" * 3) # => spamspamspam
print(4 * "2") # => 2222
```