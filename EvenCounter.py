# Write the definition and implementation of the allDigitsAreEven function here:
def allDigitsAreEven(value):
    while value > 0:
        digit = value % 10
        value = value // 10
        if digit % 2 == 0:
            result = True
            continue
        else:
            result = False
            break
    return result

# Main Program 

value = int(input())
result = allDigitsAreEven(value) # Call the allDigitsAreEven function here
if result == True:
    print ("All digits of the number",value, "are even values.")
else:
    print ("At least one digit of the number",value, "is not an even value.")