class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []


    def passenger_count(self):
        return len(self.passengers)
    

    def pick_up(self, person):
        self.passengers.append(person)
        

    def drop_off(self, person):
        self.passengers.remove(person)

        
    def empty_bus(self):
        self.passengers = []
        
   

