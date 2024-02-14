# So let's try to create a warm up project to comback for Python.

print("Hello, world!")

def myFunc1():
    i = 0
    for i in range(100):
        print(i)
    i += 1
    return 0

# myFunc1()

def myFunc2():
    i = 0
    print(
        '''
        ................
        |              |
        |  Table One   |
        |              |
        ................
        '''
    )
    # This prints multiplication table 1
    
    mult = 1
    for i in range(1, 13):
        multT = i * mult
        print(f"{i} * {mult} = {multT}")
        i += 1
        
    i += 1
    mult += 1
    
    
    print(
        '''
        ................
        |              |
        |  Table Two   |
        |              |
        ................
        '''
    )
    
    # This prints multiplication table 2
    
    mult = 2
    for i in range(1, 13):
        multT = i * mult
        print(f"{i} * {mult} = {multT}")
        i += 1
    
    i += 1
    mult += 1
    
    
    print(
        '''
        ..................
        |                |
        |  Table Three   |
        |                |
        ..................
        '''
    )
    
    # This prints multiplication table 3
    
    mult = 3
    for i in range(1, 13):
        multT = i * mult
        print(f"{i} * {mult} = {multT}")
        i += 1
    
    i += 1
    mult += 1
    
    
    print(
        '''
        ..................
        |                |
        |   Table Four   |
        |                |
        ..................
        '''
    )
    
    # This prints multiplication table 4
    
    mult = 4
    for i in range(1, 13):
        multT = i * mult
        print(f"{i} * {mult} = {multT}")
        i += 1
    
    i += 1
    mult += 1
    
    print(
        '''
        ..................
        |                |
        |   Table Five   |
        |                |
        ..................
        '''
    )
    
    # This prints multiplication table 5
    
    mult = 5
    for i in range(1, 13):
        multT = i * mult
        print(f"{i} * {mult} = {multT}")
        i += 1
    
    i += 1
    mult += 1
    
    
    
# myFunc2()

# Now that my brain's refreshed now, let's go for a little bit challenging tables program

# Take any input from user and print the multiplication table to the specified length

def myFunc3():
    
    i = int(input("Enter your desired tables value1: "))
    j = int(input("Enter your desired tables value2: "))
    k = int(input("To what value? "))
    
    for i in range(1, k+1):
        mulT = i * j
        print(f"{j} * {i} = {mulT}")
        i += 1
        
myFunc3()