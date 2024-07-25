from calc_func import addition,subtraction
def main():
    print("Welcome to the calculator app")
    func = int(input("Select the function\n 1. Add\n 2. Subtract\n"))
    A = int(input("Input the value of A-:"))
    B = int(input("Input the value of B-:"))
    if func == 1:
        print(addition(A,B))
    else:
        print(subtraction(A,B))
    
if __name__ == '__main__':
    main()