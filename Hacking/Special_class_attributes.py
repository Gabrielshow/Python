#there may be cases we jsut want the string
#indicating the type rather than an object.
stype = type('What is your quest?')
stype
print(stype.__name__)
print(type (3.1469265))