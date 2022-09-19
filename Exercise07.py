#EXERCISE 07 TUPLE, SET & DICTIONARY:
#1
season = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
month = int(input("Give me the number of a month (1-12) and I will tell you what season occurs: "))
occur = season[month-1]
print("The season occuring during month #",month, " is: ", occur)


#2

direc = set()
print("Give me names and I will tell you if I have them or not")
print("To end the program enter empty string")
name = input("Enter a name: ")
while name != "":

    if name in direc :
        print("EXISTING NAME")
    else:
        print("NEW NAME")
    direc.add(name)
    name = input("Enter a name: ")
print(direc)

#3 Problema 3 ----------------
print("Welcome to the Airport database")
data = {"EFHK" : "Helsinki-Vantaa Airport",
        "MPTO" : "Tocumen International airport",
        "KMIA" : "Miami International airport"}
option = int(input("What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
while option != 3 :
    if option == 1 :
        code = input("Enter the ICAO code of the airport: ")
        if code in data:
            print(f"The code {code} corresponds to {data[code]}")
            option = int(input(
                "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
            if option == "":
                print("PROGRAM ENDED")
                break
        else:
            print("Code was not found in the database")
            option = int(input(
                "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press 3 "))
    if option == 2 :
        print("Selected ADD")
        code = input("Add the new code: ")
        airport = input("Add the name of the airport: ")
        data[code] = airport
        print(f"The code {code} corresponds to {airport}")
        option = input(
            "What do you want to do?" "\n""To fetch data type 1""\n" "To add data type 2""\n""To quit press ENTER ")
    else:
        print("PROGRAM ENDED")
        break
print("Thank you for using the database :)")