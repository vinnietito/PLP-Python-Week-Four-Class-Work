a = 5
b = "h"

#print(a/b)
try:
    print(a/b)
    k = int(input("ENter a number: "))
except ZeroDivisionError:
    print("You can't divide this with zero")
except ValueError:
    print("We are a wrong value")
except Exception:
    print("This is a very Serious Error")
finally:
    print("Thank you for banking with us")