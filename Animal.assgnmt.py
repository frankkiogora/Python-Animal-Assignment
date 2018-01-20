# super class Animal
class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 205
    # @property 
    # uncomment @property to be able to call wal method 

    def walk(self):
        self.health -=1
        print 'walk results :', self.health
        return self

    def run(self):
        self.health -=5
        print 'Run results :', self.health
        return self

    def display_health(self):
        print "Current displayed animal health :" ,self.health

# subclass of Animal called Dog
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
        
    def pet(self):
        self.health +=5
        print "This dogs health is {} ".format(self.health)
        return self

# dog_1 = Dog("jonny")
# dog_1.pet().fly()

#  Subclass of animal called Dragon
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name) 
        self.health = 170

    def fly(self):
        self.health -=10
        print " My Dragon\'s health from Dragon fly method : {} ".format(self.health)

#  notice how I call super class with display_health method? Super solid!!!!
    def display_health(self):
        super(Dragon,self).display_health()
        print "this is a magical dragon "

animal_1 =Animal('peep')
# print animal_1.walk.walk.walk.walk
# print animal_1.run().run().run()
# print animal_1.dispay_health()
# animal_1.pet() 
# animal_1.fly()  

dragon_1= Dragon('dracula')
dragon_1.display_health()















