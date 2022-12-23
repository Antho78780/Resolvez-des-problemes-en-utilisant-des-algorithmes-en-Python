import csv
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
        return sum(total_profit)

    def calc_costs(self, combos):
        total_costs = []
        for action in combos:
            total_costs.append(action[1])
        return sum(total_costs)

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
    
    def combos(self):
        data1 = sorted(self.past_actions(self.list_actions)[0], key=lambda action: action[1], reverse=True)
        data2 = sorted(self.past_actions(self.list_actions)[1], key=lambda action: action[1], reverse=True)
        total_price1 = 0
        total_price2 = 0
        best_combos1 = []
        best_combos2 = []
        for action in data1:
            if total_price1 + action[1] <= self.WALLET and action[1] > 0:
                total_price1 += action[1]
                best_combos1.append(action)

        for action in data2:
            if total_price2 + action[1] <= self.WALLET and action[1] > 0:
                total_price2 += action[1]
                best_combos2.append(action)

        return best_combos1, best_combos2
    
    def results(self):
        combos1 = self.combos()[0]
        combos2 = self.combos()[1]
        total_costs1 = round(self.calc_costs(combos1), 2)
        total_costs2 = round(self.calc_costs(combos2), 2)
        total_profits1 = round(self.calc_profit(combos1), 2)
        total_profits2 = round(self.calc_profit(combos2), 2)
        print(f"Dataset1: prix total: {total_costs1}€, bénéfice total: {total_profits1}%")
        print(f"Dataset2: prix total: {total_costs2}€, bénéfice total: {total_profits2}%")
       


def get_data():
    list_actions = []
    for i in range(1, 3):
        with open(f"Data/dataset{i}_Python.csv", newline="") as csvFile:
            dataReader = csv.reader(csvFile, delimiter=",")
            for row in dataReader:
                action = Action(row[0], float(row[1]), float(row[2]))
                list_actions.append((action.name, action.price, action.profit))
    return list_actions

if __name__ == "__main__":
    result_data = get_data()
    action = Action_combination(result_data)
    action.results()
    