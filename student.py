class parrot:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def sing(self):
        print(f"{self.name} is singing and his color is{self.color}")

    def dance(self):
                print(f"{self.name} is dancing and his color is{self.color}")
parrot1=parrot("buddy","green")
parrot1.sing()
parrot1.dance()
parrot2=parrot("clichy","blue")
parrot2.sing()
parrot2.dance()