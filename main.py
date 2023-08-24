def main():

    celcius = int(input("Enter the temperature in celcius: "))
    fahrenheit = 9/5 * (celcius) + 32
    print (f'Fahrenheit: \t {fahrenheit:.2f}')

    # Comlete your code here
    ########################################
    # Do not delete the return statement
    ########################################
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
