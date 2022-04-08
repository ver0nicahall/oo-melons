"""Classes for melon orders."""

from random import randint
from datetime import datetime
#access day of the week 


class AbstractMelonOrder:
    """A melon order."""
    

    def __init__(self, species, qty, order_type, tax): 
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        """Get a base price."""

        timestamp = (datetime.now())
        hour = timestamp.hour
        day_of_week = (datetime.now().weekday())

        # Extra charge during morning rush hour (8-11am, Mon-Fri)
        extra_charge = 4

        #choose random integer between 5-9 as base price
        base_price = randint(5,9)

        if day_of_week in range(0,5) and hour in range(8, 11):
            base_price += extra_charge

        #if species is a Christmas melon, multiply by 1.5
        if self.species == "Christmas":
            base_price *= 1.5
        
        return base_price
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        print('base price: ', base_price)

        #flat fee: international orders with < 10 melons
        flat_fee = 0
        if self.order_type == 'international' and self.qty < 10:
            flat_fee = 3

        total = (1 + self.tax) * self.qty * base_price + flat_fee
        print('tax: ', self.tax * (base_price * self.qty))
        print('flat fee: ', flat_fee)

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'international', 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'government', 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Update inspection."""
    
        self.passed_inspection = passed 

class TooManyMelonsError(ValueError):
    super().__init__()