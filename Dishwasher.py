class Dishwasher:
    enerdgy_class = 'A'

    def __init__(self, water_consumption, programs_number, name, number_utensils_sets):
        self.water_consumption = water_consumption
        self.programs_number = programs_number
        self.name = name
        self.number_utensils_sets = number_utensils_sets 

    def __del__(self): 
        return 

    def __str__(self):
        return "\twater_consumption(liter per year): {}\n \tprograms_number: {}\n \tname: {}\n \tnumber_utensils_sets: {}".format(self.water_consumption, self.programs_number, self.name, self.number_utensils_sets)

    @staticmethod
    def getEnerdgyClass():
        return Dishwasher.enerdgy_class


if __name__ == "__main__":
    dishwasher1 = Dishwasher(3360, 5, "INDESIT", 14)
    print("The first dishwasher:\n", dishwasher1.__str__()) 

    dishwasher2 = Dishwasher(3300, 4, "BOSH", 12)
    print("The second dishwasher:\n", dishwasher2.__str__())   

    dishwasher3 = Dishwasher(2520, 6, "WHIRLPOOL", 10)
    print("The third dishwasher:\n", dishwasher3.__str__()) 

    print("Energy class of INDESIT: ", dishwasher1.getEnerdgyClass()) 