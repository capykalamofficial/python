from problem import calculate_final_price
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_tests(student_function):
    # Define test cases as (order_value, coupon_applied, expected_final_price)
    test_cases = [
        (600, False, 480.0),     # Order above $500, 20% discount
        (450, False, 405.0),     # Order between $200 and $500, 10% discount
        (150, False, 142.5),     # Order below $200, 5% discount
        (1000, True, 950.0),     # Order above $500, coupon applied, final price = 1000 - 50
        (50, True, 50.0),        # Order below $200, coupon applied, final price = max(50, 50 - 50)
        (300, True, 250.0),      # Order between $200 and $500, coupon applied, final price = 300 - 50
        (100, True, 50.0),       # Order below $200, coupon applied, final price = max(50, 100 - 50)
    ]

    # Run test cases
    print("Running tests...")
    all_passed = True
    for i, (order_value, coupon_applied, expected) in enumerate(test_cases, start=1):
        try:
            result = student_function(order_value, coupon_applied)
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
    run_tests(calculate_final_price)
