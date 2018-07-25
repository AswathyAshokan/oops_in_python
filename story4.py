from commonclass import Common
import json

class UpdateFile(Common):

    def InsertDataToFile(self,stops):
        while True:
            try:
                self.stops = stops
                self.start = input("enter source: ")
                start = self.stops[self.start]
            except KeyError:
                print("Invalid source")
                continue
            else:
                break

        while True:
            try:
                self.stops = stops
                self.end = input("enter destination: ")
                end = self.stops[self.start][self.end]
            except KeyError:
                print("Invalid source")
                continue
            else:
                break
        while True:
            try:
                self.adult = int(input("enter adult charge: "))
                if self.adult < 0:
                    raise ValueError("That is not a valid  charge!")
            except ValueError as error_message:
                print(error_message)
                continue
            else:
                break
        while True:
            try:
                self.child = int(input("enter child charge: "))
                if self.child < 0:
                    raise ValueError("That is not a valid  charge!")
            except ValueError as error_message:
                print(error_message)
                continue
            else:
                break
        self.stops[self.start][self.end]["A"] = self.adult
        modified=self.stops[self.start][self.end]
        if modified.get("C")!=None:
            self.stops[self.start][self.end]["C"]= self.child
        else:
            modified.append({"C":self.child})


        with open("ticket_charge.json", "w") as jsonFile:
            json.dump(self.stops,jsonFile)

commonClass =UpdateFile()
stops = commonClass.readFile("ticket_charge.json")
commonClass.InsertDataToFile(stops)
