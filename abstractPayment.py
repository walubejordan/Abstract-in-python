from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
    
class CreditCard(Payment):
    def make_payment(self, amount):
        print(f"Make Card payment of: {amount}")
        
class MomoPayment(Payment):
    def make_payment(self, amount):
        print(f"Make Momo payment of: {amount}")