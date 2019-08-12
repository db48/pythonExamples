def zero(a2):
    return "zero" * a2

def one(a2):
    return "one"

def tooHigh(a2):
  return "Too High!"

def numbers_to_functions_to_strings(argument, a2):
    switcher = {
        0: zero,
        1: one,
    }
    # Get the function from switcher dictionary
    # if the value is not in the dict, return the second arg
    func = switcher.get(argument, tooHigh)
    # Execute the function
    return func(a2)


def main():
  print numbers_to_functions_to_strings(0, 2)
  print numbers_to_functions_to_strings(1, 2)
  print numbers_to_functions_to_strings(2, 2)
  print numbers_to_functions_to_strings(3, 2)


if __name__ == '__main__':
	main()

