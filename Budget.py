import sys


class Application():
    def __init__(self):
        self.budget = 0
        self.expenses = 0
        self.expense_name = []
        self.expense_list = []
        self.item_name = []
        self.item_list = []
        self.prompt_budget()

    def budget_ask(self):
        add_item = input('Add a new item? [y/n]: ')
        return add_item

    def budget_sum(self):
        self.budget = sum(self.item_list)

    def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense

    def expense_sum(self):
        self.expenses = sum(self.expense_list)

    def budget_check(self):
        if not self.item_list:
            print('Please enter atleast one category of items. ')
            self.prompt_budget()

    def expense_check(self):
        if not self.expense_list:
            print('Please enter atleast one expense. ')
            self.prompt_expense()

    def prompt_budget(self):
        x = False
        while not x:
            result = self.budget_ask()
            if result == 'y':
                item_name = input('Enter an item name. [Name Only]: ')
                self.item_name.append(item_name)
                item_input = int(input('Enter amount budgeted for this item. [Numbers Only]: '))
                self.item_list.append(item_input)
            else:
                self.budget_check()
                break
        self.budget_sum()
        name = [name for name in self.item_name]
        budget = [budget for budget in self.item_list]
        incomedict = dict(zip(name, budget))
        for k in incomedict:
            print(k + ': ', '$' + str(incomedict[k]))
        print('Total user income: ', '$' + str(self.budget))
        self.prompt_expense()

    def prompt_expense(self):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':
                expense_name = input('Enter expense name. [Name Only]: ')
                while expense_name in self.item_name:
                    self.expense_name.append(expense_name)
                    break
                else:
                    expense_name = input('Enter an expense in your budget')
                expense_input = int(input('Enter expense amount. [Numbers Only]: '))
                self.expense_list.append(expense_input)
            else:
                self.expense_check()
                x = True
        self.expense_sum()
        name = [name for name in self.expense_name]
        expense = [income for income in self.expense_list]
        expensedict = dict(zip(name, expense))
        for k in expensedict:
            print(k + ': ', '$' + str(expensedict[k]))
        print('Total user expenses: ', '$' + str(self.expenses))
        self.uservalue()

    def uservalue(self):
        valoutput = self.budget - self.expenses
        if valoutput < 0:
            print('You are in the negative, you have a deficit of ' + '$' + str(valoutput))
        if valoutput == 0:
            print('You have broken even, you are spending exactly as much as you make.')
        if valoutput > 0:
            print('You are in the positive, you have a surplus of ' + '$' + str(valoutput))
        another = input('Would you like to run another analysis? [y/n]: ')
        if another == 'y':
            self.reset_program()
        elif another == 'n':
            self.close_program()

    def reset_program(self):
        self.budget = 0
        self.expenses = 0
        del self.expense_list[0:]
        del self.expense_name[0:]
        del self.item_name[0:]
        del self.item_list[0:]
        self.prompt_budget()

    def close_program(self):
        print('Exiting Program.')
        sys.exit(0)


if __name__ == '__main__':
    Application()
