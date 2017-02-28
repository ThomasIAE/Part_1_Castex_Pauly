class Bonds(object):
    """ this is a bond"""

    def __init__(self, short_bond, long_bond):
        self.long_bond = long_bond
        self.short_bond = short_bond

    def calculate_return(self, term, investment, minprice, minterm, interestrate):
        self.term = term
        self.investment = investment
        self.minprice = minprice
        self.minterm = minterm
        self.interestrate = interestrate

        return investment * ((1 + interestrate) ** term)


class short_bond(Bonds):
    def calculate_return(self, term, investment, interestrate):
        self.term = term
        self.investment = investment
        self.interestrate = interestrate
        return investment * ((1 + interestrate) ** term)


class long_bond(Bonds):
    def calculate_return(self, term, investment, interestrate):
        self.term = term
        self.investment = investment
        self.interestrate = interestrate
        return investment * ((1 + interestrate) ** term)


print(short_bond.calculate_return(100, 1000, 0,01))
print(long_bond.calculate_return(100, 3000, 0,03))

plt.grid(True)
plt.title("Investment evolution: ")
plt.plot([date])
plt.xlabel('Term')
plt.ylabel('Investment')
plt.show()