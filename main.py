# What can go wrong?


def askTheUser():
    try:
        userInput = float(input("Please enter a number to divide 100 by: "))
    except ValueError:
        print("That was not a valid number. Please try again.")
        return askTheUser()
    return userInput


def divide100ByUserInput():
    userInput = askTheUser()
    result = 100 / userInput
    return result


result100byNumber = divide100ByUserInput()

print(result100byNumber)
