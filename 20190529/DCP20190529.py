# import Timer function
from threading import Timer

# our function f which prints a simple phrase
def f():
    print("Eat cherry cheesecake!")

# number of milliseconds before function starts
n = 3000.0

# to make n in milliseconds we multiply them by 10^-3 since
#   the Timer function has inputs of seconds
t = Timer(n * (10**(-3)), f)
t.start()