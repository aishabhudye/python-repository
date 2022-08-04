class StringProcessor:

    def reverse_array(self, array_param):
        length = len(array_param)
        reversed_siblings = [""]* (length -1)
        for index in range(length - 1):
            element = array_param[index]
            print("Element at {0} is {1}".format(index, element))
            reversed_index = length - (index + 1)
            reversed_siblings[reversed_index] = element

        return reversed_siblings
