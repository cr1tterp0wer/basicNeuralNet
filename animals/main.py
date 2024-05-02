class Dog:
    """
    Dog class
    """
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp

    def status(self):
        """
        Output members
        """
        print("dog name is ", self.name)
        print("dog temperature is ", self.temperature)

    def set_temperature(self, temp):
        """
        Set Temperature
        """
        self.temperature = temp

    def bark(self):
        """
        Bark
        """
        print("woof")

sizzles = Dog('sizzle', 97)
sizzles.bark()
