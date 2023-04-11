class BusStop:

    def __init__(self, stop_name):
        self.name = stop_name
        self.queue = []

    def add_person(self, person):
        self.queue.append(person)

    def collect_passengers(self, bus):
        bus.passengers += len(self.queue)
        self.queue.clear()


