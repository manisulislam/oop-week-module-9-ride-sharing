
from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, email,nid):
        self.name= name
        self.email= email
        self.__id= 0
        self.__nid= nid
        self.wallet= 0
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

    
class Rider(User):
    def __init__(self, name, email, nid):
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"rider: with {self.name} and eamil: {self.email}")


    def request_rider(self, location, destination):
        ride_request= None
        self.current_ride=None
