def get_factorial(num):
    product = 1
    if num < 0:
        return "Invalid, you can't factorial a negative number."
    else:
        for n in range(1, num+1):
            product *= n
        return product

def sum_odd_numbers(num):
    sum = 0
    cnt = 0
    while cnt < num:
        cnt += 1
        if cnt % 2 == 1:
            sum += cnt
    
    return sum

def display_menu():
    print("Homework 3 Menu")
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - Exit")
    
def run_menu():
    display_menu()
    option = input("Select option 1, ,2, or 3: ")
    run_menu_option(option)
    
def run_menu_option(option):
    if(option == "1"):
        option_1_selected()
    elif(option == "2"):
        option_2_selected()
    elif(option == "3"):
        option_3_selected()
        
def option_1_selected():
    num = 0
    while num < 1 or num > 9:
        while True:
            try:
                num = int(input("Enter a number 1-9: "))
                break
            except ValueError:
                print("Invalid option, enter a number 1-9: ")
    
    product = get_factorial(num)
    print("The factorial of ",num,"is: ", product )
    exit_menu()
    
def option_2_selected():
    num = 0
    while num < 1 or num > 99:
        while True:
            try:
                num = int(input("Enter a number 1-99: "))
                break
            except ValueError:
                print("Invalid option, enter a number 1-99: ")

    sum = sum_odd_numbers(num)
    print("The sum of odd numbers for",num,"is:",sum)
    exit_menu()
                
def option_3_selected():
    while True:
        exit = input("Enter YES to exit, enter NO to continue")
        if exit == "YES" or exit == "yes":
            print("You have now exited.")
            break
        elif exit == "NO" or exit == "no":
            run_menu()
            break
        else:
            print("Exit? YES or NO")
        
def exit_menu():
    while True:
        continued = input("Do you wish to continue YES or NO: ")
        if continued == "YES" or continued == 'yes':
            run_menu()
            break
        elif continued == "NO" or continued == "no":
            print("You have now exited.")
            break
        else:
            print("Choose YES or NO")