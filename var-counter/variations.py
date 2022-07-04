def input_combination():
    """Input combination of letters."""
    return input("Please enter your combination: ")


def combinations_var(string):
    """
    Use cycle to generate list of
    all variants with dots inside.
     """
    i = 0   # create starting point
    combinations = []   # create empty list to save results

    while i.bit_length() < len(string):     # run while bit. number lesser than string size
        current_var = []    # create empty list to save current variant
        for item_number, item in enumerate(string):     # create loop for enumerated items
            current_var.append(item)      # append items of string to temporary list
            if (2**item_number) & i:    # find where to place dots
                current_var.append('.')     # append dots to selected positions
        i += 1  # counter
        combinations.append(''.join(current_var))   # append results of cycle to initial empty list
    return combinations


print(combinations_var(input_combination()))





