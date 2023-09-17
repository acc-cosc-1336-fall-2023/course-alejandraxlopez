import decisions

option = int(input("Enter a numerical option: "))
total = int(input("Enter a numerical total: "))

result = decisions.get_options_ratio(option, total)

print ("Your Standing is: " + decisions.get_faculty_rating(result))









