# define pair construction
def cons(a, b):
    def pair(f):
        print (a,b)
        return f(a, b)
    #print(pair)
    return pair

def car(pair):
    return pair.__closure__[0].cell_contents

def cdr(pair):
    return pair.__closure__[1].cell_contents

a=3
b=4

pair = cons(a, b)

print("Creating a pair of (", a, ", ", b, ")")
print("Calling car(pair) gives a value of ", car(pair))
print("And calling cdr(pair) gives a value of ", cdr(pair))


#def cdr(pair):
 #   return pair.b
