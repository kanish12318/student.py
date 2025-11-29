class parrot:
    speices="bird"
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def sing(self):
        print(f"{self.name} is singing and his color is{self.color}")

    def dance(self):
                print(f"{self.name} is dancing and his color is{self.color}")
parrot1=parrot("polly",1)
parrot1.sing()
parrot1.dance()
parrot2=parrot("kiwi",2)
print("parrot speices:",parrot1.speices)
parrot2.sing()
parrot2.dance()