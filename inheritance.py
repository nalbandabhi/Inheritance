class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class staff(person):
    def __init__(self,id):
        self.id=id
       
    def display(self):
       
       # print(self.name)
        super().display()
        print(self.id)
class tempstaff(staff):
    def __init__(self,name,id,hrs,days):
        person.__init__(self,name)
        staff.__init__(self,id)
        self.hrs=hrs
        self.days=days
       
    def display(self):
     
        super().display()
        print(self.hrs)
        print(self.days)  
    def sal(self):
        sl=self.hrs*self.days*150
        print(sl)
       
obj=tempstaff("tilak",12345,8,20)

obj.display()
obj.sal()