########## WE DELIVER COMPANY ############
class WeDeliver:
    def __init__(self):
        self.drivers = {
            1: {"name": "Max Verstappen", "start_city": "Akkar"},
            2: {"name": "Charles Leclerc", "start_city": "Saida"},
            3: {"name": "Lando Norris", "start_city": "Jbeil"},
            4: {"name": "Alaa Faraj", "start_city": "Beitddine"},
            5: {"name": "George Akl", "start_city": "Aley"}
        }
        self.cities = {
            "Akkar": ["Jbeil", "Tripoli", "Zahle"],
            "Saida": ["Beirut"],
            "Jbeil": ["Akkar", "Beirut", "Tripoli"],
            "Beirut": ["Saida", "Jbeil"],
            "Zahle": ["Jbeil", "Akkar", "Tripoli"],
            "Tripoli": ["Akkar", "Jbeil", "Zahle"],
            "Beitddine": ["Barouk"],
            "Aley": ["Beirut"],
            "Barouk": ["Beitddine"]
        }
        def main_menu(self):
            while True:
                print("Hello! Please enter: ")
                print("1. To go to the drivers' menu")
                print("2. To go to the cities' menu")
                print("3. To exit the system")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                        self.drivers_menu()
                elif choice == "2":
                        self.cities_menu()
                elif choice == "3":
                        print("Exiting the system. Goodbye!")
                        break
                else:
                        print("Invalid input! Please try again.")
        def drivers_menu(self):
            stop=False
            while not stop:
                print("Enter: ")
                print("1. To view all the drivers")
                print("2. To add a driver")
                print("3. To go back to the main menu")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                        self.view_drivers()
                elif choice == "2":
                        self.add_driver()
                elif choice == "3":
                        stop=True
                else:
                    print("Invalid input! Please try again.")
        def view_drivers(self):
            for key, value in self.drivers.items():
                print(f"{key:03d}, {value['name']}, start city: {value['start_city']}")
        def add_driver(self):
            driver_name = input("Enter the name of the driver you want to add: ").strip()
            start_city = input("Enter the start city of this driver: ").strip().capitalize()
            if start_city not in self.cities:
             add_city = input("City not found in the database! Would you like to add it? (yes/no): ").strip().lower()
            if add_city == "yes":
                neighbors = input(f"Enter the names of the neighboring cities for {start_city} (comma separated): ").strip().capitalize().split(", ")
                self.cities[start_city] = neighbors
            for neighbor in neighbors:
                    if neighbor not in self.cities:
                        self.cities[neighbor] = [start_city]
                    else:
                        self.cities[neighbor].append(start_city)
            else:
                print("Driver not added.")
                return 

