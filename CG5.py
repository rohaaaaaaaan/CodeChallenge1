def check_fermat(a, b, c, n):
    # Step 1: Check if n > 2
    if n > 2:
        # Step 2: Check if the equation a^n + b^n = c^n holds
        if a**n + b**n == c**n:
            # Step 3: Print if the equation holds true
            print("Holy smokes, Fermat was wrong!")
        else:
            # Step 4: Print if the equation does not hold
            print("No, that doesn’t work.")
    else:
        # Step 5: If n <= 2, print a message that doesn't work
        print("No, that doesn’t work.")
