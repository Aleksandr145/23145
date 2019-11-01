 # calculate v2

what = input( "What do it? (+,-,/,*): " )

a = float( input("Input one nuber: ") )
b = float( input("Input two nuber: ") )

if what == "+":
    c = a + b
    print("Answer: " + str(c))
    input()
elif what == "-":
    c = a - b
    print("Answer: " + str(c))
    input()
elif what == "*":
    c = a * b
    print("Answer: " + str(c))
    input()
elif what == "/":
    c = a / b
    print("Answer: " + str(c))
    input()	
else:
    print("Error!!!!!")

    input()