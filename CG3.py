# Function to print 'spam' or any given string twice
def print_twice(message):
    print(message)
    print(message)

# Modified do_twice to take a function and a value and call the function twice
def do_twice(f, v):
    f(v)
    f(v)

# Call do_twice to print 'spam' twice
do_twice(print_twice, 'spam')

# Function to call a function four times
def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

# Call do_four to print 'spam' four times
do_four(print_twice, 'spam')
