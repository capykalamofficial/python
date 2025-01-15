from problem import check_ride_eligibility
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (height, accompanied_by_adult, expected_eligibility)
    test_cases = [
        (120, False, True),    # Exactly 120 cm, allowed to ride alone
        (115, True, True),     # Between 110 and 119 cm, with an adult, allowed
        (100, True, False),    # Less than 110 cm, even with an adult, not allowed
        (150, False, True),    # Greater than 120 cm, allowed to ride alone
        (200, False, False),   # Exactly 200 cm, not allowed for safety
        (205, False, False),   # Greater than 200 cm, not allowed for safety
        (110, True, False),    # Exactly 110 cm, not allowed even with an adult
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (height, accompanied_by_adult, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(height, accompanied_by_adult)
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
    run_tests(check_ride_eligibility)
