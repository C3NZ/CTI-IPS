def fizzbuzz(n):
    """
    Your typical fizzbuzz problem

    Args:
        n - The number we're trying to fizz buzz up till.

    Returns:
        Nothing, but prints output according to the rules of fizzbuzz
    """
    for current_number in range(1, n + 1):
        if current_number % 5 == 0 and current_number % 3 == 0:
            print("fizzbuzz")
        elif current_number % 5 == 0:
            print("buzz")
        elif current_number % 3 == 0:
            print("fizz")
        else:
            print(current_number)


# Please do not modify the code below this line.
# When you run your code, you will need to enter
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)
