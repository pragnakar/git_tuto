class first_class():

    def __init__(self):
        print("inititalizing a class")

    def first_function(self):
        print('first function')

if __name__ == '__main__':
    obj = first_class()
    obj.first_function()
    obj.function_in_branch()
    # removed the added function in branch
