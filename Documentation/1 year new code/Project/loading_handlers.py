
class Loading_Handlers():
    def loading_handlers_in_array(self,name):
        array = []
        with open(name + '.txt') as f:
            array = f.readlines()

        for i,string in enumerate(array):
            array[i] = string.strip('\n')

        return array