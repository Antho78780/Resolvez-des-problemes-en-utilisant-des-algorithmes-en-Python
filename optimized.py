import csv
class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
    
    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}€, profit: {self.profit}%"
        

def get_data():
    list_actions = []
    for i in range(1, 3):
        with open(f"Data/dataset{i}_Python.csv", newline="") as csvFile:
            dataReader = csv.reader(csvFile, delimiter=",")
            for row in dataReader:
                action = Action(row[0], row[1], row[2])
                list_actions.append((action.name, action.price, action.profit))
    return list_actions

if __name__ == "__main__":
    result_data = get_data()