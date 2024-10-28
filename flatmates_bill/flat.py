class Bill:
    """This is a class to store the bill amount and billing period."""
    def __init__(self, amount, period):
        self.period = period  # The period of the bill (e.g., "March 2024").
        self.amount = amount  # The total amount of the bill.

class Flatmate:
    """This is a class to represent a flatmate and calculate their share of the bill."""
    def __init__(self, name, days_in_house):
        self.name = name  # The name of the flatmate.
        self.days_in_house = days_in_house  # The number of days the flatmate stayed in the house.

    def pays(self, bill, flatmate_in_house):
        """This method calculates how much the flatmate needs to pay based on their stay duration."""
        weight = self.days_in_house / (self.days_in_house + flatmate_in_house.days_in_house)
        to_pay = bill.amount * weight  # The flatmate's share of the total bill.
        return to_pay