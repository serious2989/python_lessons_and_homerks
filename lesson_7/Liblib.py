def hi():
    print("Hi!")

def simple():
    num = int(input("Enter a num: "))
    return num ** 5 + 14

if __name__ == "__main__":
    print("I a file")
    simple()
else:
    print("I a module")
