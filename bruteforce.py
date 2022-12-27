import csv
from itertools import combinations
import time
class Action:
    def __init__(self, name, price, percentage_benefit):
        self.name = name
        self.price = price
        self.percentage_benefit = percentage_benefit

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, profit: {self.percentage_benefit}"  

class ActionCombination:
    def __init__(self, list_action, max_invest=500):
        self.actions = list_action
        self.max_invest = max_invest
        
    def get_all_combinations(self):
        best_combos = []
        profit = 0
        costs = 0
        for i in range(len(self.actions)):
            combos = combinations(self.actions, i+1)
            for combo in combos:
                if self.calc_costs(combo) <= self.max_invest:
                    costs = self.calc_costs(combo)
                    profit = self.calc_profits(combo)
                    best_combos = combo
        return [best_combos, profit, costs]

    def calc_profits(self, combos):
        profits = []
        for combo in combos:
            ben = combo[1] * combo[2] / 100
            profits.append(ben)
        return sum(profits)

    def calc_costs(self, combos):
        costs = []
        for combo in combos:
            costs.append(combo[1])
        return sum(costs)
    
    def results_actions(self):
        results_actions = self.get_all_combinations()[0]
        for result in results_actions:
            print('\033[93m',result, '\033[0m')

def get_data():
    with open("data/dataTest.csv", newline='') as csvFile:
        dataReader = csv.reader(csvFile, delimiter=',')
        list_actions = []
        for row in dataReader:
            action = Action(row[0], float(row[1]), float(row[2]))
            print('\033[91m', action, '\033[0m')
            list_actions.append((action.name, action.price, action.percentage_benefit))
        return list_actions

def main():
    result_data = get_data()
    combination = ActionCombination(result_data)
    print('\033[92m'f'Il y a {len(result_data)} actions dans la base de donnée')
    print(f"Le bénéfice total est de {combination.get_all_combinations()[1]}%")
    print(f"Le coût total est de {combination.get_all_combinations()[2]}€")
    print("Les actions les plus rentables: "'\033[0m')
    combination.results_actions()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    temps = round(end - start, 3)
    print(f"Temps exécuté: {temps}secondes")
