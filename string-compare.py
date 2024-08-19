# In this lab we will ask the user for two string inputs and compare them

while True:
    # get the string inputs
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")

    # check for quit condition
    if string1.lower() == "quit" or string2.lower() == "quit":
        break
    # strings are equal
    elif string1 == string2:
        print(f"The strings '{string1}' and '{string2}' are the same.")
    # strings are not equal
    elif string1 != string2:
        print(f"The strings1 '{string1}' and '{string2}' are different.")


