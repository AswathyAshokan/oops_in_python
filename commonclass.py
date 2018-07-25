import json
class Common:
    def InsertData(self, stops):

        print("inside function")
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
                self.stops = stops
                self.age = int(input("enter age: "))
                if self.age <= 0:
                    raise ValueError("That is not a valid  age!")
            except ValueError as error_message:
                print(error_message)
                continue
            else:
                break
    def readFile(self,filename):
        self.filename=filename
        with open(self.filename) as f:
            data = json.load(f)
        return data

    def total_fare(self, stops):
        print("erroeeee")
        self.stops = stops
        print(self.stops)
        childValue =self.stops[self.start][self.end]
        c_val =childValue.get("C")
        fare = self.stops[self.start][self.end]["A"]
        if self.age < 5:
            fare = 0
        elif self.age > 60:
            fare = 50 / 100 * fare
        elif self.age < 13 and c_val == None:
            fare = 50 / 100 * fare
        elif self.age < 13 and c_val != None:
            fare = self.stops[self.start][self.end]["C"]
        return fare

    def discountData(self,stops):
        self.stops = stops
        while True:
            try:

                self.start = input("enter source: ")
                startValue = stops[self.start]
            except KeyError:
                print("Invalid source")
                continue
            else:
                break

        while True:
            try:
                self.end = input("enter destination: ")
                endValue = stops[self.start][self.end]
            except KeyError:
                print("Invalid source")
                continue
            else:
                break
        while True:
            try:
                self.number = int(input("enter number of passengers: "))
                if self.number <= 0:
                    raise ValueError("That is not a valid  number!")
            except ValueError as error_message:
                print(error_message)
                continue
            else:
                break
        fareList = []
        withoutDiscount =[]
        for i in range(1, self.number + 1):
            while True:
                try:
                    self.age = int(input("enter the age : "))
                    if self.age <= 0:
                        raise ValueError("That is not a valid  age!")
                    else:
                        fare = self.total_fare(stops)
                        withoutDiscount.append(fare)
                        if self.age>13 and self.start =="Stop-3" and self.end =="Stop-4"and self.number>2:
                            fare=fare-20/100*fare
                        elif self.age <=13 and self.start =="Stop-4" and self.end =="Stop-1"and self.number>2:
                            fare=fare-20/100*fare
                        fareList.append(fare)
                except ValueError as error_message:
                    print(error_message)
                    continue
                else:
                    break
        '''displaying the totalfare and discount fare'''
        totalBusfare = 0
        totalDiscountFare = 0
        for fareValue in withoutDiscount:
            totalBusfare = totalBusfare + fareValue
        for discountValue in fareList:
            totalDiscountFare = totalDiscountFare + discountValue

        if self.number>2 and self.start == "Stop-1"and self.end =="Stop-3":
            total=0
            for fareCharge in withoutDiscount:
                total=total+fareCharge
            discount=total-20/100*total
            print("Total Fare :",total)
            print("Discount Fare :",discount)
        elif totalBusfare == totalDiscountFare:
            print("Total Fare :",totalBusfare)
            print("Discount Fare  : N0 DISCOUNT")
        else:
            print("Total Fare :",totalBusfare)
            print("Discount Fare :",totalDiscountFare)
