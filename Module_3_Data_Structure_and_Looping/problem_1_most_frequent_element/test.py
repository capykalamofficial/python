from problem import most_frequent_element
from colorama import Fore, init

init(autoreset=True)

def run_tests(student_function):
    test_cases = [
        ([1, 2, 2, 3, 1, 2], 2),
        (['apple', 'banana', 'apple', 'cherry'], 'apple'),
        ([3, 3, 4, 4], 3),  # Tie: 3 and 4 both appear twice; 3 appears first
        ([1], 1),
        (['x', 'y', 'x', 'z', 'x', 'y'], 'x')
    ]

    print("Running tests...")
    all_passed = True
    for i, (input_list, expected) in enumerate(test_cases, 1):
        try:
            result = student_function(input_list)
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
    run_tests(most_frequent_element)
