class Student():
    name=None
    age = 18
    course="Python"
    def doHomeWork(self):
        print (self.name ,"do ",self.course)
    pass;
s=Student();
s.name="zyl"


print( Student.__dict__)