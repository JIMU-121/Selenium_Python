
class RateOfInterest:

    def __int__(self, name, loan, interest):
        self.name = name
        self.loan = loan
        self.interest = interest

    def calc_interest(self, loan: object, Interest):
        print("Total Interest: ", self.loan * self.interest)


p1 = RateOfInterest()
p1.calc_interest(6, 5)