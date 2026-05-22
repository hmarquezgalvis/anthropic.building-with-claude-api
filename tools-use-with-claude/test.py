import sys
from main import calculate_pi_to_5_digits

def test_pi_calculation():
    """Test the pi calculation function."""
    pi_value = calculate_pi_to_5_digits()
    expected_pi = 3.14159
    
    print(f"Calculated pi: {pi_value}")
    print(f"Expected pi (to 5 digits): {expected_pi}")
    
    # Check if the result matches the expected value to 5 decimal places
    if pi_value == expected_pi:
        print("✓ Test PASSED: Pi calculated correctly to 5 decimal places")
        return True
    else:
        print("✗ Test FAILED: Pi calculation does not match expected value")
        print(f"  Difference: {abs(pi_value - expected_pi)}")
        return False

def test_pi_range():
    """Test that pi is within the expected range."""
    pi_value = calculate_pi_to_5_digits()
    
    # Pi should be between 3.14159 and 3.14160
    if 3.14159 <= pi_value <= 3.14160:
        print("✓ Test PASSED: Pi is within the expected range (3.14159-3.14160)")
        return True
    else:
        print("✗ Test FAILED: Pi is outside the expected range")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Pi Calculation Function")
    print("=" * 50)
    print()
    
    # Run tests
    test1_passed = test_pi_calculation()
    print()
    test2_passed = test_pi_range()
    
    print()
    print("=" * 50)
    if test1_passed and test2_passed:
        print("All tests PASSED! ✓")
        sys.exit(0)
    else:
        print("Some tests FAILED! ✗")
        sys.exit(1)
