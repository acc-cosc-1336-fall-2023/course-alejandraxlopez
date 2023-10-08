#
def get_hamming_distance(dna1, dna2):
    distance = 0
    #strings should be same length
    for i in range(len(dna1)):
       if dna1[i] != dna2[i]:
          distance += 1
    return distance


def get_dna_complement(dna):
    dna = dna.upper()
    verify = verify_dna(dna)
    if verify == 'DNA':
        complement = dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
        complement = complement.upper()
        reverse = complement[::-1]
        return reverse
    else:
        return "Invalid"

def display_menu():
    print("1 - Hamming Distance")
    print("2 - DNA Complement")
    print("3 - Exit")

def run_menu():
    display_menu()
    option = str(input("Select option 1, 2, or 3: "))
    while (option != '1' and option != '2' and option != '3'):
        option = str(input("Invalid. Select 1, 2, or 3: "))
    select_option(option)

def select_option(option):
    if option =='1':
        option_1()
    if option =='2':
        option_2()
    if option =='3':
        option_3()

def option_1():
    print("Option 1 Selected, Enter two strings of equal to find the Hamming Distance")
    x = str(input("Enter 1st String: "))
    y = str(input("Enter 2nd String: "))
    z = get_hamming_distance(x, y)
    while z == 'Invalid':
        print("Unequal string length")
        x = str(input("Enter 1st String: "))
        y = str(input("Enter 2nd String: "))
        z = get_hamming_distance(x,y)
    print(f"The Hamming Distance is {z}")
    option_3()

def option_2():
    print("Option 2 Selected, Enter DNA strand")
    x = str(input('Enter DNA Strand '))
    z = get_dna_complement(x)
    while z == 'Invalid':
        print("Invalid strand, input new DNA strand")
        x = str(input('Enter DNA Strand'))
        z = get_dna_complement(x)
    print("The reverse complement of",x,"is",z)
    option_3()

def option_3():
    while True:
        exit = str(input("Exit? Y or N: "))
        if exit == 'y' or exit == 'Y':
            print("Exiting Program")
            break
        elif exit == 'n' or exit == 'N':
            run_menu()
            break
        else:
            print("Invalid, Select Y or N")

def verify_dna(dna):
    dna = dna.upper()
    count = 0
    if dna == '':
        return 'Invalid'
    for letter in range(len(dna)):
        if dna[letter] == 'A' or dna[letter] == 'T' or dna[letter] == 'C' or dna[letter] =='G':
            count += 1
    if count != len(dna):
        return 'Invalid'
    else:
        return 'DNA'
