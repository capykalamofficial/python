from problem import sum_even_fibonacci
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    test_cases = [
        (10, 10),              # 2 + 8 = 10
        (1, 0),                # No even numbers ≤ 1
        (34, 44),              # 2 + 8 + 34 = 44
        (60, 44),              # next even fib is 144 > 60, so answer stays 44
        (1000, 798),           # Even fib numbers ≤ 1000: 2, 8, 34, 144, 610
        (4000000, 4613732)     # Classic Project Euler test case
    ]

    print("Running tests...")
    all_passed = True
    for i, (limit, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(limit)
            assert result == expected, f"Test case {i} failed: result: {result}, expected: {expected}"
            print(f"{Fore.GREEN}Test case {i} passed!")
        except Exception as e:
            all_passed = False
            print(f"{Fore.RED}Test case {i} failed: {e}")

    if all_passed:
        print(f"{Fore.GREEN}All test cases passed!")
    else:
        print(f"{Fore.RED}Some test cases failed.")

if __name__ == "__main__":
    run_tests(sum_even_fibonacci)
