################################
# Github Repo link
# Your Name
# Your Section 
# Your Student ID Number
################################
# REFERENCES
# https://www.youtube.com/watch?v=fEp5nWvujhI
################################
# SOLUTION
# Your Solution Score: <total sum>
################################

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_sum(lines):
    total_sum = 0  # Initialize total sum to 0
    for line_number, line in enumerate(lines, start=1):  # Iterate through each line with line numbers
        digits = [int(char) for char in line if char.isdigit()]  # Filter out non-digit characters
        if len(digits) >= 2:  # Ensure there are at least two digits in the line
            first_digit = digits[0]  # Extract the first digit
            last_digit = digits[-1]  # Extract the last digit
            number = first_digit * 10 + last_digit  # Combine the digits to form a two-digit number
            print(f"Line {line_number}: {first_digit}{last_digit} ({first_digit} + {last_digit})")  # Print the number being added
            total_sum += number  # Add the two-digit number to the total sum
    return total_sum


if __name__ == "__main__":
    file_name = "364.txt"
    lines = read_input(file_name)
    total_sum = calculate_sum(lines)
    print("The total sum from the given input file", file_name, "is", total_sum)
