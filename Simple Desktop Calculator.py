a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Enter your operator: ")
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "/":
        print(a/b)
    case "*":
        print(a*b)
    case "%":
        print(a%b)
    case "//":
        print(a//b)
    