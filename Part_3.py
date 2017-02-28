class Investors(object):
    """ this is a bond"""

    def __init__(self,aggressive, defensive, mixed):
        self.aggressive = aggressive
        self.defensive = defensive
        self.mixed = mixed

    class aggresive(Investors):
        def calculate_(self, term, investment, interestrate):