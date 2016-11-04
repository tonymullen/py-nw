
def myfunc(arg):
    print(arg)
    return('Return string ' + arg)

if __name__ == '__main__':
    functionalVar = myfunc('Hi there, FP')
    print(functionalVar) # calls function and prints return value
