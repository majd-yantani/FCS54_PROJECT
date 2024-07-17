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