import argparse

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate factorial.')
    parser.add_argument('-n', '--number', type=int, help='number for factorial calculation')
    args = parser.parse_args()
    
    if args.number is None:
        # Solicitar al usuario que ingrese un número si no se proporciona como argumento
        user_input = input("Ingrese un número: ")
        args.number = int(user_input)
    
    result = factorial(args.number)
    print("El factorial de", args.number, "es", result)