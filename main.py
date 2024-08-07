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
        while True:
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
                break
            else:
                print("Invalid input! Please try again.")

    def view_drivers(self):
        for key, value in self.drivers.items():
            print(f"{key:03d}, {value['name']}, start city: {value['start_city']}")

    def add_driver(self):
        while True:
            driver_name = input("Enter the name of the driver you want to add: ").strip()
            if not driver_name.replace(' ', '').isalpha(): 
                print("Invalid name! Please enter a valid name containing only letters.")
                continue
            
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
                    print(f"City {start_city} added with neighbors {', '.join(neighbors)}.")
                else:
                    print("Driver not added.")
                    return 
            new_id = max(self.drivers.keys()) + 1
            self.drivers[new_id] = {"name": driver_name, "start_city": start_city}
            print(f"Driver {driver_name} added with new ID {new_id:03d}.")
            break


    def cities_menu(self):
        while True:
            print("Enter:")
            print("1. Show cities")
            print("2. Print neighboring cities")
            print("3. Print drivers delivering to city")
            print("4. Go back to the main menu")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.show_cities()
            elif choice == "2":
                self.neighboring_cities()
            elif choice == "3":
                self.print_drivers_delivering()
            elif choice == "4":
                break
            else:
                print("Invalid input! Please try again.")

    def show_cities(self):
        print("Cities in the system:")
        for city in self.cities.keys():
            print(city)

    def neighboring_cities(self):
        city = input("Enter the name of the city you want to know the neighboring cities of: ").strip().capitalize()
        if city in self.cities:
            print(f"The neighboring cities are: {', '.join(self.cities[city])}")
        else:
            print("City not found in the database!")

    def print_drivers_delivering(self):
        city = input("Enter the name of the city to list drivers delivering to: ").strip().capitalize()
        delivering_drivers = []

        reachable_cities = self.bfs_reachable_cities(city)
        for driver_id, info in self.drivers.items():
            if info['start_city'] in reachable_cities:
                delivering_drivers.append(info['name'])

        if delivering_drivers:
            print(f"Drivers delivering to {city}: {', '.join(delivering_drivers)}")
        else:
            print(f"No drivers can deliver to {city}.")

    def bfs_reachable_cities(self, start_city):
        if start_city not in self.cities:
            return set()

        visited = set()
        queue = [start_city]

        while queue:
            current_city = queue.pop(0)
            if current_city not in visited:
                visited.add(current_city)
                for neighbor in self.cities[current_city]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited


we_deliver = WeDeliver()
we_deliver.main_menu()