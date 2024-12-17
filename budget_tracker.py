class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = float(0)

    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self):
        res = ''
        star_len = 30 - len(self.name)
        title = '*'*(star_len//2) + self.name
        if star_len%2 == 0:
            title += '*'*(star_len//2)
        else:
            title += '*'*(star_len+1)
        res += title + '\n'
        
        for item in self.ledger:
            amt = str('{:.2f}'.format(item['amount'])).rjust(7)
            desc =  item['description'][:23].ljust(23)
            res += desc+amt
            res += '\n'
        
        bal = '{:.2f}'.format(self.get_balance())
        res += 'Total: ' + bal

        return res

def create_spend_chart(categories):
    names = [category.name for category in categories]
    # percents to be calculated only from withdrawls
    amounts = []
    for category in categories:
        amt = 0
        for item in category.ledger:
            if item['amount'] < 0:
                amt += abs(item['amount'])
        amounts.append(amt)

    total_spent = sum(amounts)
    # finding floor of percent to the nearest 10s value
    percent_spent = [ (((amt/total_spent)*100)/10)*10  for amt in amounts ]
    
    res = 'Percentage spent by category\n'
    # iterate for all percent values
    for val in range(100, -10, -10):
        res += str(val).rjust(3) + '|'
        # iterate for all the categories
        for p in percent_spent:
            res += ' o ' if val <= p else '   '
        res += ' \n'
        
    # append mid lines
    res += ' '*4 + '---'*(len(names)) + '-\n'
    
    # add names in vertical format
    mx_len = max( len(name) for name in names )
    # iterate over index of max length
    for idx in range(mx_len):
        # iterate over the names
        res += ' '*4
        for name in names:
            res += f' {name[idx]} ' if idx < len(name) else '   '
        # additonal space at last to pass test
        res += ' '
        # new line not needed on the last line
        if idx < mx_len-1:
            res += '\n'

    return res

    
# a = Category('Food')
# b = Category('Travel')

# a.deposit(110.27, 'snacks')
# a.deposit(200, 'lunch')
# a.withdraw(50, 'had breakfast')

# b.deposit(500, 'tickets')
# a.transfer(100, b)
# b.withdraw(100, 'cab charges')

# bar_chart = create_spend_chart([a, b])
# print(bar_chart)


