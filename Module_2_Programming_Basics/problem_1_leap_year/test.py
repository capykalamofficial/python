from problem import is_leap_year
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (input_year, expected_result)
    test_cases = [
        (2024, True),          # Typical leap year
        (1900, False),         # Divisible by 100 but not by 400
        (2000, True),          # Divisible by 400
        (2023, False),         # Not divisible by 4
        (2400, True),          # Future leap year
        (1800, False)          # Divisible by 100 but not 400
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (year, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(year)
            assert result == expected, f"Test case {i} failed: result: {result}, expected: {expected}"
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
    run_tests(is_leap_year)
