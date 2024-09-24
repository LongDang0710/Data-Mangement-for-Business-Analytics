# 1. Add a PMT method to class Loan
class Loan:
    def __init__(self, principal, annual_rate, term_years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.term_years = term_years

    def pmt(self):
        monthly_rate = self.annual_rate / 12
        total_payments = self.term_years * 12
        pmt = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
        return pmt

# Example
loan = Loan(25000, 0.05, 3)
print(f"Monthly payment: {loan.pmt():.2f}")

# 2. Create a class for cash flows. Add a NPV method
class CashFlow:
    def __init__(self, cash_flows):
        self.cash_flows = cash_flows

    def npv(self, discount_rate):
        npv_value = 0
        for t, cf in enumerate(self.cash_flows):
            npv_value += cf / (1 + discount_rate) ** t
        return npv_value

# Example
cash_flows = [-10000, 3000, 4000, 5000]
cf = CashFlow(cash_flows)
print(f"NPV: {cf.npv(0.1):.2f}")

# 3. Using objects of class Point, determine the distance between two points (-10,5) and (0, 10)
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example
point1 = Point(-10, 5)
point2 = Point(0, 10)
print(f"Distance between points: {point1.distance(point2):.2f}")
