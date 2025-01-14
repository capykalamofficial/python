# test_calculate_discount.py

from problem import calculate_discounted_price
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (input, expected_output) tuples
    test_cases = [
        # (amount, discount, expected discounted price)
        (100, 0, 100.0),          # No discount
        (100, 100, 0.0),          # Full discount
        (200, 15, 10.0),         # 15% discount
        (50, 5, 47.5),            # Small discount
        (1000, 50, 500.0),        # 50% discount
        (0, 50, 0.0)              # No amount
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (amount, discount, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(amount, discount)
            assert result == expected, f"Test case {i} failed: result : {result} expected : {expected}"
            print(f"{Fore.GREEN}Test case {i} passed!")
        except Exception as e:
            all_passed = False
            print(f"{Fore.RED}Test case {i} failed: {e}")
    
    if all_passed:
        print(f"{Fore.GREEN}All test cases passed!")
    else:
        print(f"{Fore.RED}Some test cases failed.")

# Run the tests with the student function
if __name__ == "__main__":
    run_tests(calculate_discounted_price)
