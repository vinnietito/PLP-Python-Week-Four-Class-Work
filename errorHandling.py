a = 5
b = 3

#print(a/b)
try:
    print(a/b)
    k = int(input("Enter a number: "))
except ZeroDivisionError:
    print("You can't divide this with zero")
except ValueError:
    print("We are a wrong value")
except Exception:
    print("This is a very Serious Error")
finally:
    print("Thank you for banking with us")