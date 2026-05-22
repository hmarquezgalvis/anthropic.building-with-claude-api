def greeting():
  print("Hello world!")


def calculate_pi_to_5_digits():
    """
    Calculate pi to the 5th decimal digit (3.14159...).
    Uses the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to get 5 accurate decimal places
    getcontext().prec = 50
    
    def arctan(x, num_terms):
        """Calculate arctan(x) using Taylor series."""
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    x = Decimal(1) / Decimal(5)
    y = Decimal(1) / Decimal(239)
    
    pi = 4 * (4 * arctan(x, 100) - arctan(y, 100))
    
    # Round to 5 decimal places
    return float(round(pi, 5))