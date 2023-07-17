
while 2 > 0:
    print("**************Hello to Automata Project**************")
    print("*****************************************************")
    print("1. Design a finite automaton (FA)")
    print("2. Test if a FA is deterministic or non-deterministic")
    print("3. Test if a string is accepted by a FA")
    print("4. Construct an equivalent DFA from NFA")
    print("5. Minimize a DFA")
    print("*****************************************************")
    n = int(input("Please input a program number: "))
    if n == 1:
        print("*****************************************************")
        print("1. Design a finite automaton (FA)")
        exec(open('App.py').read())
        print("*****************************************************")
    elif n == 2:
        print("*****************************************************")
        print("2. Test if a FA is deterministic or non-deterministic")
        exec(open('App.py').read())
        print("*****************************************************")
    elif n == 3:
        print("*****************************************************")
        print("3. Test if a string is accepted by a FA")
        exec(open('testPython/NFA2DFA.py').read())
        print("*****************************************************")
    elif n == 4:
        print("*****************************************************")
        print("4. Construct an equivalent DFA from NFA")
        exec(open('testPython/stringCheck_constDFA.py').read())
        print("*****************************************************")
    elif n == 5:
        print("*****************************************************")
        print("5. Minimize a DFA")
        print("program is to be determine")
        print("*****************************************************")
    