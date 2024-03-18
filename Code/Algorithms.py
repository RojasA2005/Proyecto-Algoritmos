import json

def selection_sort(my_list):
    length = len(my_list)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if my_list[min_index][-1] > my_list[j][-1]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

def binary_search(my_list, name):
    if len(my_list) == 0:
        return None
    mid = len(my_list) // 2
    if my_list[mid][-1] == name:
        return get_similar_elements(my_list, mid)
    elif name < my_list[mid][-1]:
        return binary_search(my_list[0:mid], name)
    else:
        return binary_search(my_list[mid+1:], name)
    
def linear_search(my_list, id):
    for element in my_list:
        if id == element[0]:
            return element

def insertion(direction, id, name):
    with open(direction) as file:
            file_content = json.load(file)
            search_list = file_content
    for i in range(len(search_list)):
        if name < search_list[i][-1]:
            search_list.insert(i, [id, name])
            break
    with open(direction, "w") as file:
        json.dump(search_list, file)

def get_similar_elements(my_list, index):
    similar = []
    list_reversed = my_list[:index]
    list_reversed.reverse()
    for element in list_reversed:
        if element[-1] == my_list[index][-1]:
            similar.append(element[0])
        else:
            break
    similar.append(my_list[index][0])
    for element in my_list[index+1:]:
        if element[-1] == my_list[index][-1]:
            similar.append(element[0])
        else:
            break
    return similar


