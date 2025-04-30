from problem import is_palindrome
from colorama import Fore, init

init(autoreset=True)

def run_tests(student_function):
    test_cases = [
        ("Racecar", True),
        ("python", False),
        ("Madam", True),
        ("hello", False),
        ("A", True),
        ("", True),
        ("level", True)
    ]

    print("Running tests...")
    all_passed = True
    for i, (word, expected) in enumerate(test_cases, 1):
        try:
            result = student_function(word)
            assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"
            print(f"{Fore.GREEN}Test case {i} passed!")
        except Exception as e:
            all_passed = False
            print(f"{Fore.RED}Test case {i} failed: {e}")

    if all_passed:
        print(f"{Fore.GREEN}All test cases passed!")
    else:
        print(f"{Fore.RED}Some test cases failed.")

if __name__ == "__main__":
    run_tests(is_palindrome)
