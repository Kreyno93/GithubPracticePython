# What can go wrong?
# I need to divide a number by the user input

# Where is my entry point ?


def askTheUser():
    try:
        userInput = float(input("Please enter a number to divide 100 by: "))
    except ValueError:
        print("That was not a valid number. Please try again.")
        return askTheUser()
    return userInput


def divide100ByUserInput():  # 100 / by the user Input || Example : 100 / 25 = 4
    userInput = askTheUser()
    result = 100 / userInput  # User Input = 25
    return result


result = divide100ByUserInput()

# or

resultOfDivide100ByUserInputFunction = divide100ByUserInput()
# at the end these are just variables / placeholders to store the data
# for the program, it doesnt care what name these are (as long as the names are valid)
# but for us, the programmers/developers it does matter. It easier to identify

print(result)
print(resultOfDivide100ByUserInputFunction)
