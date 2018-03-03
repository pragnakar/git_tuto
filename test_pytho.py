class first_class():

    def __init__(self):
        print("inititalizing a class")

    def first_function(self):
        print('first function')
    def third_function(self,a,b):
            return a*b

if __name__ == '__main__':
    obj = first_class()
    obj.first_function()
    print("this is a third branch")
    # push from atom
    print(obj.third_function())
    # adding a comment 
