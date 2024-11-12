from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def make_service(self, service):
        pass
    
class WheelAnglinement(Service):
    def make_service(self, service):
        print(f"Adjusting Wheel anglinment of: {service}")
        
class TirePressure(Service):
    def make_service(self, service):
        print(f"Adjusting Tire Pressure: {service}")
        
class ChangeOil(Service):
    def make_service(self, service):
        print(f"Changing Oil: {service}")
        
service1 = WheelAnglinement()
service1.make_service('back tiers')