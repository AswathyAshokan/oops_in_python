from commonclass import Common
stops = {
        "Stop-1": {"Stop-1": {"A": 0}, "Stop-2": {"A": 10, "C": 6}, "Stop-3": {"A": 30}, "Stop-4": {"A": 45},
                   "Stop-5": {"A": 60}},
        "Stop-2": {"Stop-1": {"A": 50}, "Stop-2": {"A": 0}, "Stop-3": {"A": 60, "C": 40}, "Stop-4": {"A": 80},
                   "Stop-5": {"A": 70}},
        "Stop-3": {"Stop-1": {"A": 80}, "Stop-2": {"A": 70}, "Stop-3": {"A": 0}, "Stop-4": {"A": 40, "C": 20},
                   "Stop-5": {"A": 20}},
        "Stop-4": {"Stop-1": {"A": 90}, "Stop-2": {"A": 30}, "Stop-3": {"A": 10}, "Stop-4": {"A": 0},
                   "Stop-5": {"A": 50}},
        "Stop-5": {"Stop-1": {"A": 100}, "Stop-2": {"A": 20}, "Stop-3": {"A": 5}, "Stop-4": {"A": 60, "C": 20},
                   "Stop-5": 0}
    }


commonValue =Common()
commonValue.discountData(stops)
