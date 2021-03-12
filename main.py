from itertools import permutations

sexy_list = list(permutations(range(4), 4))

all_the_amounts = []

my_num = 1001

print(sexy_list)


def is_all_same(num_in):
    for i in num_in:
        if not num_in[0] == i:
            return False
    return True

while my_num < 10000:
    print("top")
    print(my_num)

    num_of_fun_string = 0

    my_num_stringified = str(my_num)

    if is_all_same(my_num_stringified):
        print("continued")
        my_num += 11
        continue

    for i in sexy_list:
        fun_string = ""
        #print(str(i) + " i")
        for ii in i:
            #print(str(ii) + " ii")
            fun_string += my_num_stringified[ii]
        #print("fun str out " + str(fun_string))

        if int(fun_string) % 11 == 0:
            print("fun str " + str(fun_string))
            num_of_fun_string += 1

    print("amount " + str(num_of_fun_string))
    all_the_amounts.append(num_of_fun_string)
    my_num += 11


no_duplicates = []

for i in all_the_amounts:
    pp = False
    for ii in no_duplicates:
        if ii == i:
            pp = True
    if not pp:
        no_duplicates.append(i)

print(no_duplicates)
