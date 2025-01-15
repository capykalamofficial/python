from problem import calculate_total_amount
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (principal, rate, years, expected_total_amount)
    test_cases = [
        (1000.0, 5.0, 2, 1102.5),        # Simple interest case
        (1500.0, 4.0, 3, 1680.0),        # Another case with different principal and rate
        (2000.0, 0.0, 5, 2000.0),        # Zero interest
        (5000.0, 10.0, 1, 5500.0),       # High interest for 1 year
        (10000.0, 7.5, 10, 21144.4),     # Longer period with moderate interest
        (0.0, 5.0, 5, 0.0),              # Zero principal
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (principal, rate, years, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(principal, rate, years)
            assert round(result, 2) == round(expected, 2), f"Test case {i} failed: result: {result}, expected: {expected}"
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
    run_tests(calculate_total_amount)
