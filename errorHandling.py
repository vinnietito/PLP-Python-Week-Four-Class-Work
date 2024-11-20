a = 5
b = "h"

#print(a/b)
try:
    print(a/b)
except ZeroDivisionError:
    print("You can't divide this with zero")
except Exception:
    print("This is a very Serious Error")