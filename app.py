from calc_func import addition,subtraction
from multiply import multiplication
def main():
    print("Welcome to the calculator app")
    func = int(input("Select the function\n 1. Add\n 2. Subtract\n 3.Mutiply\n"))
    A = int(input("Input the value of A-:"))
    B = int(input("Input the value of B-:"))
    if func == 1:
        print(addition(A,B))
    elif func==2:
        print(subtraction(A,B))
    
    elif func == 3:
        print(multiplication(A,B))
    
    
if __name__ == '__main__':
    main()