x = 0 # global

def siguiente():
    x = 1 # local
    return x

def anterior():
    global x # global
    x = -1 
    return x
#siguiente()
anterior()
print(x)