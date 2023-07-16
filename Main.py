

while 2 > 0:
    print("Hello to Automata Project")
    print("1. N")
    print("2. N")
    print("3. N")
    print("4. N")
    print("5. N")
    n = int(input("Please input a program number: "))
    if n == 1:
        exec(open('App.py').read())
    elif n == 2:
        print("Hello this is")
    elif n == 3:
        exec(open('testPython/NFA2DFA.py').read())
    elif n == 4:
        exec(open('testPython/stringCheck_constDFA.py').read())
    elif n == 5:
        print("5")
    