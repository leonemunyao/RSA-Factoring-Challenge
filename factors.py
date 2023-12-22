import sys

def factorize(n):
    # Function to factorize a number into two smaller numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer
                number = int(line.strip())
                
                # Factorize the number
                factor1, factor2 = factorize(number)

                # Print the factorization in the required format
                if factor1 is not None and factor2 is not None:
                    print(f"{number}={factor1}*{factor2}")
                else:
                    print(f"Unable to factorize {number}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
