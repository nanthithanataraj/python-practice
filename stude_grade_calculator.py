marks = int(input("Enter the marks(1-100) : "))
if (marks>=90):
    print("A")
elif (marks>=75) or (marks<=89):
    print("B")
elif (marks>=50) or (marks<=74):
    print("C")
else:
    print("Fail")