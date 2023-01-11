import csv
import time
import tracemalloc
class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
    
    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}€, profit: {self.profit}%"
        
class Action_combination:
    def __init__(self, list_actions, wallet=500):
        self.list_actions = list_actions
        self.WALLET = wallet

    def calc_profit(self, combos):
        total_profit = []
        for action in combos:
            ben = action[1] * action[2] / 100
            total_profit.append(ben)
        return round(sum(total_profit), 2)

    def calc_costs(self, combos):
        total_costs = []
        for action in combos:
            total_costs.append(action[1])
        return round(sum(total_costs), 2)

    def past_actions(self, actions):
        numberLine = 0
        list_actions1 = []
        list_actions2 = []
        for i in actions:
            numberLine += 1
            if numberLine <= 1001:
                list_actions1.append(i)
            if numberLine > 1001:
                list_actions2.append(i)
        return list_actions1, list_actions2

    def combos(self, action):
        data = sorted(action, key=lambda action: action[1], reverse=True)
        total_price = 0
        best_combos = []
        for a in data:
            if total_price + a[1] <= self.WALLET and a[1] > 0:
                total_price += a[1]
                best_combos.append(a)
        total_costs = self.calc_costs(best_combos)
        total_profits = self.calc_profit(best_combos)
        return best_combos, total_costs, total_profits

    def print_dataset(self, dataset, cost, profit, chr):
        if len(dataset) <= 1:
                print('\033[92m' f"{chr}: {len(dataset)} élément")
        else:
            print('\033[92m' f"{chr}: {len(dataset)} éléments")
        for action in dataset:
                print(action)
        print('\033[92m' f"prix total: {cost}€, bénéfice total: {profit}%" '\033[0m')


    def results(self):
        dataset1 = self.combos(self.past_actions(self.list_actions)[0])
        dataset2 = self.combos(self.past_actions(self.list_actions)[1])
        self.print_dataset(dataset1[0], dataset1[1], dataset1[2], "Dataset1")
        self.print_dataset(dataset2[0], dataset2[1], dataset2[2], "Dataset2")

def get_data():
    list_actions = []
    for i in range(1, 3):
        with open(f"Data/dataset{i}_Python.csv", newline="") as csvFile:
            dataReader = csv.reader(csvFile, delimiter=",")
            for row in dataReader:
                action = Action(row[0], float(row[1]), float(row[2]))
                list_actions.append((action.name, action.price, action.profit))
    return list_actions

def main():
    result_data = get_data()
    action = Action_combination(result_data)
    action.results()
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    temps = round(end - start, 3)
    print(f"Temps exécuté: {temps} secondes")