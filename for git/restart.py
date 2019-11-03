# first asking about age
name = input("Give me your name: ")
age = int(input("Enter your age: " ))
year = str((2010 - age)+100)
print("Dear, " + name + "."'\n'"Will be 100 years old in the years " + year + ('\n'"Be careful !!!"))
input("                              Good luck my frend !!!") # more free place for beutiful

answer = str(raw_input('Run again? (y/n): '))

if answer == 'n':
   print('Goodbye')
   break
elif answer == 'y':
   #restart_program???
else:
   print('Invalid input.')
