class Rooms:
    def __init__(self, floorNum, roomNum, view, suite, status, arrival, departure):
        self.floorNum = floorNum
        self.roomNum = roomNum
        #Note: view -- if roomNum%2 == 0: view = "Ocean Side" else: view = "Court Yard" return view
        self.view = view
        #Note: suite -- if roomNum <= 2: suite = "Room is a suite" elif rumNum >= 19: suite = "Room is a suite" else: suite = "Room is not a suite"
        self.suite = suite
        self.status = status
        self.arrival = arrival
        self.departure = departure

    def displayRooms(self):
        #print("Floor: ", self.floorNum, ", Room: ", self.roomNum, ", ")
        print("Floor: ", self.floorNum, "\nRoom: ", self.roomNum, "\nView: ", self.view, "\nSuite: ", self.suite, "\nStatus: ", self.status, "\nDate: ", self.arrival, " - ", self.departure)

Room1 = Rooms(1,1,"Ocean","True","Occupied","September 15, 2021","September 18, 2021")
Room1.displayRooms()
