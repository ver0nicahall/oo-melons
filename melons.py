"""Classes for melon orders."""

class AbstractMelonOrder:
    """A melon order."""
    

    def __init__(self, species, qty, order_type, tax): 
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        #if species is a Christmas melon
        if self.species == "Christmas":
            base_price *= 1.5
        
        #flat fee: international orders with < 10 melons
        flat_fee = 0
        if self.order_type == 'international' and self.qty < 10:
            flat_fee = 3

        total = (1 + self.tax) * self.qty * base_price + flat_fee

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