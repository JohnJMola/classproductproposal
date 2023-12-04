import numpy as np
import matplotlib as plt

def cMode():
    print("Calculations Mode")
    prob = ""
    while prob != "q":
        try:
            print("Enter problem")
            prob=input()
            print(eval(bytes*[ord(p) for p in prob]))
        except:
            if prob !="q":
                print("invalid input")

def gMode():
    print("graph mode")
    eq,r1,r2="",0,0
    while eq !="q":
        try:
            print("enter equation")
            eq=input()
            if eq=="q":
                break
            print("Enter range 1")
            r1=input()
            if r1=="q":
                break
            else:
                r1=int(r1)
            print("Enter range 2")
            r2=input()
            if r2=="q":
                break
            else:
                r2=int(r2)
            x=np.array(range(int(r1),int(r2)))
            y=eval(bytes([ord(p)for p in eq]))
            plt.plot(x,y)
            plt.show()
        except:
            if eq !="q":
                print("invalid input")

mode=""

while mode !="q":
    print("""
          1. c (Normal calculation)
          2. g (Graphing)
          3. h (Help)
          4. q (Quit)
          """)
    mode=input().lower()
    if mode=="c":
        cMode()
    if mode=="g":
        gMode()
    if mode=="h":
        print("""
            1. Do not use parentheses while multiplying
            2. Put 'np.' before using any of the NUMPY functions.
              """)
