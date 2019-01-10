##########################################################################################################################
#
# The restaurant booking system can only handle bookings on tier 1 and tier 2 cities.
# This custom LocationSlot will validate the user input with the list of supported cities
# from a csv and set slot with three possible “values”, which is represented with a vector of length 2.
#
# Return Values:
#          (0,0)	not yet set
#          (1,0)	city supported
#          (0,1)	the city is not in the supported city list
#
###########################################################################################################################
from rasa_core.slots import Slot

class LocationSlot(Slot):

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            # The file supported_cities.txt contains the list of tier 1 and tier 2 cities india taken from below link. 
            # http://en.wikipedia.org/wiki/Classification_of_Indian_cities
            # Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z.
            # Consider 'X ' cities as tier-1 and 'Y' as tier-2.
            city_list = []
            filename = "data\lookup_tables\supported_cities.txt"
            with open(filename) as data:
                datalines = (line.rstrip('\r\n') for line in data)
                for line in datalines:
                    city_list.append(line.lower())
            
            if self.value.lower() in city_list:
                r[0] = 1.0
            else:
                r[1] = 1.0
        return r



