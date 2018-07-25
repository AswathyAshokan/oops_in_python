
from commonclass import Common
totalCharge =Common()
stops=totalCharge.readFile("ticket_charge.json")
print(stops)
print(totalCharge.InsertData(stops))
print(totalCharge.total_fare(stops))
