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
    ans = obj.third_function(3,4)
    print(ans)
    # adding a comment
    #added a comment from vs code

#%%
print("hello world")
a = input('enter a: ')
print(a)