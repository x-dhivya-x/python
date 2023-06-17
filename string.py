a='Hello World'
print(len(a))   #len function

#string methods
"""a.upper()
   a.lower()
   a.find("H")  it will tell that which index the H occur
   a.replace("H","G")
   a.title()
"""
print(type(a))
print(a.count('l'))

#Ascii value

print(ord('D'))
print(ord(chr(65)))
print(chr(97))

#Check the string(specific word is present or not)

txt = "The best things in life are expensive!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
else:
	print("expensive is present")

#String slicing(get the range of characters)

b="Jagatheeshwaran"
print(b[1:7])
print(b[ :7])
print(b[0: ])
print(b[ : ])
print(b[-5:-1])
print(b[ : :1])

#strip (remove whitespace before and after the text)

a = " Hello, Dhivya "
print(a)
print(len(a))
print(a.strip())
print(len(a.strip()))




