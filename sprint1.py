from commonclass import Common
stops = {
        "Stop-1": {"Stop-1": 0, "Stop-2": 10, "Stop-3": 30, "Stop-4": 45, "Stop-5": 60},
        "Stop-2": {"Stop-1": 50, "Stop-2": 0, "Stop-3": 60, "Stop-4": 80, "Stop-5": 70},
        "Stop-3": {"Stop-1": 80, "Stop-2": 70, "Stop-3": 0, "Stop-4": 40, "Stop-5": 20},
        "Stop-4": {"Stop-1": 90, "Stop-2": 30, "Stop-3": 10, "Stop-4": 0, "Stop-5": 50},
        "Stop-5": {"Stop-1": 100, "Stop-2": 20, "Stop-3": 5, "Stop-4": 60, "Stop-5": 0}
    }



class TotalCharge(Common):
    def train_fare(self):
        fare = self.stops[self.start][self.end]
        if self.age > 60 or self.age < 13:
            fare =50/100*fare
        return fare
fare_value = TotalCharge()
print("case1")
fare_value.InsertData(stops)
print("case2")
print(fare_value.train_fare())
