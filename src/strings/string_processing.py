def reverse_array(array_param):
    length = len(array_param)
    reversed_siblings = []
    for index in range(length):
        reversed_index = length - (index + 1)
        element = array_param[reversed_index]
        reversed_siblings.append(element)

    return reversed_siblings
