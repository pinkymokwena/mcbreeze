#class fruit:
     #def __init__ (self):
         #self.name="apple"
         #self.color="green"

#my_fruit=fruit()
#print(my_fruit.color)
     
class fruit:
      def __init__ (self,name):
        self.name = name
        

      def details(self):
          print("my fruit is " + self.name)

apple=fruit("red")
apple.details()
