# Define the Knight class

class Knight:

    # Define the constructor to initialize the Knight object with the given properties

    def __init__(self, name, weapon_type, armour_material, heroic_status, horse_name):

        self.name = name

        self.weapon_type = weapon_type

        self.armour_material = armour_material

        self.heroic_status = heroic_status

        self.horse_name = horse_name

    # Define the string representation of the Knight object

    def __str__(self):

       return f"{self.name} ({self.weapon_type}, {self.armour_material}, Heroic status: {self.heroic_status}/10, Horse name: {self.horse_name})"

 # Define the function to view all the knights in the list

def get_heroic_status():
    
    while True:
        heroic_status = input("Enter heroic status out of 10: ")
        if heroic_status.isnumeric():
            heroic_status = int(heroic_status)
            if 0 <= heroic_status <= 10:
                return heroic_status
        print("Invalid input. Please enter an integer value between 0 and 10.")

# Define the function to add a new knight to the list of knights

def add_knight(knights):
    knight = []
    
    name = input("Enter knight's name: ")
    while True:
        weapon_type = input("Enter weapon type: ")
        if weapon_type.isalpha():
            break
        print("Invalid input. Please enter letters only.")
        
    while True:
        armour_material = input("Enter armour type: ")
        if armour_material.isalpha():
            break
        print("Invalid input. Please enter letters only.")
        
    heroic_status = get_heroic_status()
    horse_name = input("Enter horse name: ")
    
    knight.append(name)
    knight.append(weapon_type)
    knight.append(armour_material)
    knight.append(heroic_status)
    knight.append(horse_name)
    
    knights.append(knight)
    
    print(f"{name} added to the list of knights.\n")

# Define the function to edit a knight's details in the list

def edit_knight(knights):
    if knights:
        print("List of knights:")
        for i, knight in enumerate(knights):
            print(f"{i+1}. {Knight(knight[0], knight[1], knight[2], knight[3], knight[4])}")
        while True:
            try:
                index = int(input("Enter the index of the knight to edit: ")) - 1
                if index < 0 or index >= len(knights):
                    print("Invalid index. Please enter a valid index.\n")
                else:
                    knight = knights[index]
                    break
            except ValueError:
                print("Invalid input. Please enter an integer value for the index.\n")
        name = input("Enter knight's name: ")
        while True:
            weapon_type = input("Enter weapon type: ")
            if weapon_type.isalpha():
                break
            print("Invalid input. Please enter letters only.")
            
        while True:
            armour_material = input("Enter armour type: ")
            if armour_material.isalpha():
                break
            print("Invalid input. Please enter letters only.")
        
        heroic_status = get_heroic_status()
        horse_name = input("Enter horse name: ")
        knight[0] = name
        knight[1] = weapon_type
        knight[2] = armour_material
        knight[3] = heroic_status
        knight[4] = horse_name
        print(f"{name} updated in the list of knights.\n")
    else:
        print("No knights added yet.\n")

# View knights created

def view_knights(knights):
    if knights:

        print("List of knights:")

        for i, knight in enumerate(knights):

            print(f"{i+1}. {Knight(knight[0], knight[1], knight[2], knight[3], knight[4])}")

        print("")

    else:

        print("No knights added yet.\n")


# Define the main function to run the program

def main():

    knights = []

    while True:

        # Print the menu options

        print("1. Add a knight")

        print("2. View knights")

        print("3. Edit a knight")

        print("4. Exit")

        # Get user input for their choice

        choice = input("Enter choice (1/2/3/4): ")

 

        # Handle the different menu choices

        if choice == "1":

            add_knight(knights)

        elif choice == "2":

            view_knights(knights)

        elif choice == "3":

            edit_knight(knights)

        elif choice == "4":

            print("Good Bye")
            break

        else:

            print("Invalid choice. Please enter a valid choice.\n")

 

if __name__ == "__main__":

    main()