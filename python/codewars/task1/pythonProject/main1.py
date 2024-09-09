# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

def sum_to_binary(a, b):
    sum_result = a + b
    result_binary = bin(sum_result)[2:]
    return result_binary

if __name__ == "__main__":
    print(sum_to_binary(a=5, b=6))