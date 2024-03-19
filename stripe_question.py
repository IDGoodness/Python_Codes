'''

Given an interger n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

'''
def longest_consecutive_ones(n):
    # Convert the integer to binary and split it into a list of characters
    binary = [int(x) for x in bin(n)[2:]]

    # Initialize the current run and maximum run to 0
    current_run = 0
    max_run = 0

    # Iterate over the binary digits
    for digit in binary:
        # If the digit is 1, increment the current run
        if digit == 1:
            current_run += 1
        # If the digit is 0, update the maximum run if necessary
        else:
            max_run = max(max_run, current_run)
            current_run = 0

    # Return the maximum run, including the possible final run
    return max(max_run, current_run)


num = int(input("Enter number: "))
result = longest_consecutive_ones(num)
print(result)



# Here is an alternative approach to solve this problem in Python:

def longest_consecutive_ones(n):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(n)[2:]

    # Split the binary string into a list of characters
    binary_list = list(binary)

    # Initialize the current run and maximum run to 0
    current_run = 0
    max_run = 0

    # Iterate over the binary digits
    for i in range(len(binary_list)):
        # If the digit is 1, increment the current run
        if binary_list[i] == '1':
            current_run += 1
        # If the digit is 0, update the maximum run if necessary
        else:
            max_run = max(max_run, current_run)
            current_run = 0

    # Return the maximum run, including the possible final run
    return max(max_run, current_run)