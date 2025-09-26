from fractions import Fraction
import math

def solve_proportion(a, b, c):
    """Solve the proportion a/b = c/x for x."""
    return (b * c) / a

def solve_for_x(equation):
    """Solve for x in a simple linear equation of the form ax + b = c."""
    # Example input: "2x + 3 = 7"
    left, right = equation.split('=')
    left = left.strip()
    right = float(right.strip())
    
    # Extract coefficients
    if 'x' in left:
        parts = left.replace('x', ' * x').split('+')
        a = float(parts[0].strip().split('*')[0]) if '*' in parts[0] else 1.0
        b = float(parts[1].strip()) if len(parts) > 1 else 0.0
        return (right - b) / a
    else:
        raise ValueError("The equation must contain 'x'.")

def factor_square_root(n):
    """Factor the square root of a number."""
    if n < 0:
        return "Complex number"
    root = math.sqrt(n)
    return root

def decimal_to_fraction(decimal):
    """Convert a decimal to a fraction."""
    return Fraction(decimal).limit_denominator()

def decimal_to_percent(decimal):
    """Convert a decimal to a percent."""
    return decimal * 100

def fraction_to_decimal(fraction):
    """Convert a fraction to a decimal."""
    return float(fraction)

def fraction_to_percent(fraction):
    """Convert a fraction to a percent."""
    return float(fraction) * 100

def percent_to_decimal(percent):
    """Convert a percent to a decimal."""
    return percent / 100

def percent_to_fraction(percent):
    """Convert a percent to a fraction."""
    return Fraction(percent, 100).limit_denominator()

def main():
    print("Multi-Function Calculator")
    print("1. Solve Proportions")
    print("2. Solve for x in Equations")
    print("3. Factor Square Roots")
    print("4. Convert Decimals to Fractions and Percents")
    print("5. Convert Fractions to Decimals and Percents")
    print("6. Convert Percents to Decimals and Fractions")
    
    choice = input("Select an option (1-6): ")
    
    if choice == '1':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        x = solve_proportion(a, b, c)
        print(f"The value of x is: {x}")
    
    elif choice == '2':
        equation = input("Enter the equation (e.g., 2x + 3 = 7): ")
        x = solve_for_x(equation)
        print(f"The value of x is: {x}")
    
    elif choice == '3':
        n = float(input("Enter a number to factor the square root: "))
        result = factor_square_root(n)
        print(f"The square root of {n} is: {result}")
    
    elif choice == '4':
        decimal = float(input("Enter a decimal: "))
        fraction = decimal_to_fraction(decimal)
        percent = decimal_to_percent(decimal)
        print(f"The fraction is: {fraction}, The percent is: {percent}%")
    
    elif choice == '5':
        fraction_input = input("Enter a fraction (e.g., 1/2): ")
        fraction_obj = Fraction(fraction_input)
        decimal = fraction_to_decimal(fraction_obj)
        percent = fraction_to_percent(fraction_obj)
        print(f"The decimal is: {decimal}, The percent is: {percent}%")
    
    elif choice == '6':
        percent = float(input("Enter a percent: "))
        decimal = percent_to_decimal(percent)
        fraction = percent_to_fraction(percent)
        print(f"The decimal is: {decimal}, The fraction is: {fraction}")
    
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()