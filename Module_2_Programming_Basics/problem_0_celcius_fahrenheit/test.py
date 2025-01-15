from problem import celsius_to_fahrenheit
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (input_celsius, expected_fahrenheit)
    test_cases = [
        (0, 32.0),             # Freezing point of water
        (100, 212.0),          # Boiling point of water
        (-40, -40.0),          # Same in both scales
        (37, 98.6),            # Average human body temperature
        (-273.15, -459.67)     # Absolute zero
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (celsius, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(celsius)
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
    run_tests(celsius_to_fahrenheit)
