class Entry:
    def __init__(self):
        pass
        
    def readLine(self, line):
        name = ""
        date = ""
        finishedName = False

        for char in line:
            if char.isdigit():
                finishedName = True

            if not finishedName:
                name += char
            else:
                date += char


        self.name = name.rstrip()
        self.date = date

    def createManually(self, first_name, last_name, date_of_birth):
        self.name = last_name+", "+first_name
        self.date = date_of_birth

class Entries:
    def __init__(self):
        self.entries = []
        with open('data.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                entry = Entry()
                entry.readLine(line)
                self.addEntry(entry, False)

    
    def addEntry(self,entry, addToFile):
        if addToFile:
            with open('data.txt','a') as f:
                f.write("\n"+entry.name+" "+entry.date)
        self.entries.append(entry)

    def findByName(self,toFind):
        people = []
        for entry in self.entries:
            if toFind.lower() in entry.name.lower():
                people.append(entry)
        return people
    
    def findByMonth(self,month):
        people = []
        for entry in self.entries:
            if month in entry.date[3:5]:
                people.append(entry)
        return people
    
    def viewAll(self):
        people = []
        for entry in self.entries:
            people.append(entry)
        return people

entries = Entries()

def menu():
    print("Register Reader System")
    print("-----------------------")
    print("Select an option:")
    print("1. View All Names/Birthdays")
    print("2. View People by Birth Month")
    print("3. Search by Name")
    print("4. Add to Register")
    print("5. Exit")
    print("-----------------------")
    while True:
        choice = input("Select an option: ")
        if choice.isdigit() and len(choice) == 1:
            if int(choice) > 0 and int(choice) < 5:
                print()
                return int(choice)
            else:
                print("Invalid choice. Try again\n")
        else:
            print("Invalid choice. Try again\n")

def main():
    choice = menu()
    match choice:
        case 1:
            print("Names:")
            print("-----------------------")
            people = entries.viewAll()
            if people == []:
                print("No one found.")
            for person in people:
                print(person.name,person.date)
            print("-----------------------")
            print()
            main()
        case 2:
            while True:
                month = input("Enter the month in XX format (e.g. January is 01): ")
                if month.isdigit() and len(month) == 2:
                    if int(month[0]) == 0 or int(month[0]) == 1:
                        break
                    else:
                        print("Invalid month entry.\n")
                else:
                    print("Invalid month entry.\n")
            people = entries.findByMonth(month)
            print()
            if people == []:
                print("No one found.")
            for person in people:
                print(person.name,person.date)
            print()
            main()
        case 3:
            name = input("What name to find? ")
            people = entries.findByName(name)
            print()
            if people == []:
                print("No one found.")
            for person in people:
                print(person.name,person.date)
            print()
            main()
        case 4:
            firstName = input("Enter the person's first name: ")
            lastName = input("Enter the person's last name: ")
            while True:
                day = input("Enter the day in XX format (e.g. First day is 01): ")
                if day.isdigit() and len(day) == 2:
                    if int(day[0]) > -1 or int(day[0]) < 4:
                        break
                    else:
                        print("Invalid day entry.\n")
                else:
                    print("Invalid day entry.\n")
            while True:
                month = input("Enter the month in XX format (e.g. January is 01): ")
                if month.isdigit() and len(month) == 2:
                    if int(month[0]) > -1 or int(month[0]) < 4:
                        break
                    else:
                        print("Invalid month entry.\n")
                else:
                    print("Invalid month entry.\n")
            while True:
                year = input("Enter the year in XXXX format (e.g. 1984): ")
                if year.isdigit() and len(year) == 4:
                    break
                else:
                    print("Invalid year entry.\n")
            print()
            dateOfBirth = day+"/"+month+"/"+year
            new_person = Entry()
            new_person.createManually(firstName, lastName,dateOfBirth)
            entries.addEntry(new_person, True)
            print("Added",firstName,lastName,"to the register.\n")
            main()
        case 5:
            quit()
        
main()
