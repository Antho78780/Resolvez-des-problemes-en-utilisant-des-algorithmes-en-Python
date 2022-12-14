import csv
from itertools import combinations
from tqdm import tqdm
costs = []
action = [("Action1", 20),("Action2", 30),("Action3", 40),("Action4", 50)]


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
        combos = combinations(self.actions, 2)

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
#    def get_all_combinations(self, number_action=2, all_combinations=[]):
#         all_combinations.append(list(itertools.combinations(self.actions, number_action)))
#         return self.get_all_combinations(number_action - 1, all_combinations)


def get_data():
    with open("data/dataTest.csv", newline='') as csvFile:
        dataReader = csv.reader(csvFile, delimiter=',')
        list_actions = []
        for row in dataReader:
            action = Action(row[0], float(row[1]), float(row[2]))
            list_actions.append((action.name, action.price, action.percentage_benefit))
        return list_actions


def main():
    result_data = get_data()
    print(f'Il y a {len(result_data)} actions')
    combination = ActionCombination(result_data)
    combination.get_all_combinations()
    
if __name__ == "__main__":
    main()
