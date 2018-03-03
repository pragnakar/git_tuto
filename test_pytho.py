class first_class():

    def __init__(self):
        print("inititalizing a class")

    def first_function(self):
        print('first function')
    def function_in_branch(self):
        print("this is a function in branch")
        return None
if __name__ == '__main__':
    obj = first_class()
    obj.first_function()
    obj.function_in_branch()
    # removed commmit
