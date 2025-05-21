#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string to convert.

    Returns:
        int: The integer representation of the Roman numeral, or 0 if input is
        invalid.
    """
    if not roman_string or not isinstance(roman_string, str):
        return 0

    # Dictionary to map Roman numerals to integers
    dic_x = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    total = 0
    # Iterate over each character in the Roman numeral string
    for i in range(len(roman_string)):
        # If the current value is greater than the previous value,
        # it means we have a subtractive combination (like IV or IX)
        if i > 0 and dic_x[roman_string[i]] > dic_x[roman_string[i - 1]]:
            total += dic_x[roman_string[i]] - 2 * dic_x[roman_string[i - 1]]
        else:
            total += dic_x[roman_string[i]]
    return total
