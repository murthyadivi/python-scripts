# returns the number input by user

def input_number(prompt):
    return int(input(prompt))
    
    
# Checks if the given number is a primer or not
def check_prime(number):
 
#Default primes
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
        
#Test for all all other numbers    
    else:
        prime = True
        for check_number in range(2, (number // 2)+1):
            if number % check_number == 0:
                prime = False
                break
    return prime

def display_prime(number):
    prime = check_prime(number)
    if prime:
        check = ""
    else:
        check = "not "
    print("The given number, ", number," is ", check, "prime.", sep = "", end = "\n\n")
    
while 1 == 1:
    display_prime(input_number("Enter a number to check. Ctl-C to exit: "))
