from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start, end, distance):
        self.start_place = start
        self.end_place = end
        self.distance = distance
    @abstractmethod
    def cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
    def cost(self):
        return 0
    

class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
    def cost(self):
        return 40 * self.distance
    

class Train(Transportation):
    def __init__(self, start, end, distance, station):
        super().__init__(start, end, distance)
        self.station = station
    def cost(self):
        return self.station * 5
    
def main():
    trip1 = Walk("Home", "School", 3)
    trip2 = Taxi("Home", "School", 3)
    trip3 = Train("Home", "School", 3, 2)
    trips = [trip1, trip2, trip3]
    for i in range(len(trips)):
        print(f"Trip {i} cost {trips[i].cost()}")

main()