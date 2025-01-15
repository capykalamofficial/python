from problem import calculate_final_grade
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (score1, score2, score3, score4, expected_grade)
    test_cases = [
        (95, 85, 92, 88, "A"),
        (78, 85, 80, 74, "C"),
        (56, 60, 65, 58, "F"),
        (88, 90, 92, 85, "B"),
        (60, 62, 61, 59, "D"),
        (100, 100, 100, 100, "A"),
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (score1, score2, score3, score4, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(score1, score2, score3, score4)
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
    run_tests(calculate_final_grade)
