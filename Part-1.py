import matplotlib.pyplot as plt  # Import matplotlib
import matplotlib

#Create a class for each type of bond and a method to compute the return
class short_bond(object):
    def __init__(self, name):
        self.name = name

    def calculate_return(self, term, investment, interest_rate):
        self.term = term
        self.investment = investment
        self.interest_rate = interest_rate
        return investment * ((1 + interest_rate) ** term)

class long_bond(object):
    def __init__(self, name):
        self.name = name

    def calculate_return(self, term, investment, interest_rate):
        self.term = term
        self.investment = investment
        self.interest_rate = interest_rate
        return investment * ((1 + interest_rate) ** term)

bond1 = short_bond("bond1")
bond2 = long_bond("bond2")

#add the returns for each year until the 100th year
bond1_return = []
bond2_return = []
for x in range(2, 101):
    bond1_return.append(bond1.calculate_return(x, 1000, 0.01))
for y in range(5, 101):
    bond2_return.append(bond2.calculate_return(y, 3000, 0.03))

#print(bond1_return)
#print(bond2_return)

#plot the list you want
plt.plot(bond2_return)
plt.title('Long term bond return')
plt.show()