class PublicCity:

    #contructor
    def __init__(self, place_name, population, area):
        self.place_name = place_name
        self.population = population
        self.area = area

    #plublic function
    def publicPlaceName(self):
        
        #accessing public data
        print("Place: ", self.place_name)

#creating object of the class
place1 = PublicCity("Toronto", 3000000, 630.18)

#calling public function
place1.publicPlaceName()

#accessing public data
print("Population: ", place1.population, "\nArea in km^2: ", place1.area)
    
class ProtectedCity:

    #conctructor with protected data
    def __init__(self, place_name, population, area): 
        self._place_name = place_name
        self._population = population
        self._area = area

    #protected function
    def _ProtectedPopulation(self):

        #acessing protected data
        print("Population: ", self._population)
        print("Area in km^2: ", self._area)

#creating object
place2 = ProtectedCity("Berlin", 3600000, 891.7)

#accessing prtected data
print("Place: ", place2._place_name)

#calling protected function
place2._ProtectedPopulation()



