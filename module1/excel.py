def excel_column_to_number(column):
    """
    Converting an excel column into a digit that represents the column

    Args:
        column - The column as a string

    Returns:
        the column number
    """
    # Empty column
    if not column:
        return 0

    # Setup initial variables
    magnitude = len(column) - 1
    column_num = 0

    # Iterate through the characters inside of the column
    for char in column:
        # The column number is the ascii representation, shifted by 64 and then
        # multiplied by the alchemy
        column_num += (ord(char) - 64) * (26 ** magnitude)
        magnitude -= 1

    return column_num


print(excel_column_to_number("A"))
