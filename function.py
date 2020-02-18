# ---------1st Program-----------------
def nameoffunction(argument):
    first = argument + 2
    return first


variable = nameoffunction(6)
print(variable)


# ---------2nd Program-----------------
def equals_str(input_lst, input_str):  # formal arguments
    if input_lst[0] == input_str:
        return True
    else:
        return False


movieList = ['abc', 'xyz', 'mnp']
userinput = 'abc'
print(equals_str(movieList, userinput))  # actual aarguments
print(equals_str(input_str=userinput, input_lst=movieList))


# 2nd Function
def counter(item):
    return len(item)


print("------default arguments------")


def eveningBatch(name1='Hitesh', name2='Shivam'):
    string = "{},{} are Very Good Students".format(name1, name2)
    return string


# main program

print(eveningBatch())
print(eveningBatch('a', 'b'))


def eveningBatch(c, d, name1='Hitesh', name2='Shivam'):
    string = "{},{} are Very Good Students".format(name1, name2)
    return string


# main program

print(eveningBatch('a', 'b'))


# 1st function
def list_counter(input_lst):
    final_list = []
    for each in input_lst:
        num_elt = counter(each)
        print(num_elt)
        final_list.append(num_elt)
    return final_list


# main program
lists = [["dog", "cat", "rabbit"], [True[1, 2, 3, 4], ]]
# print(len(lists[1]))
list_count = (list_counter(lists))
print(list_count)

print("-----use of lambda function------")
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
aynomous = list(map(lambda x: (x % 2 == 0), my_list))
aynomous2 = list(filter(lambda x: (x % 2 == 0), my_list))
print(aynomous)
print(aynomous2)

