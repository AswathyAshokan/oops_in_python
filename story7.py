from commonclass import Common
discount =Common()
stops=discount.readFile("ticket_charge.json")
discount.discountData(stops)