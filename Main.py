from operator import sub

def is_spiral(first_num, last_num):
    if (first_num != 0 or last_num != 0) and (first_num and last_num <= 1000) and (first_num != last_num):
        return shortest_distance(first_num, last_num)

def shortest_distance(first_num: int, last_num: int, spiral=[[0, 0, 0] * 2]):
    transforms = ((1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1))

    for i in range(max(first_num, last_num)):
        for index, values in enumerate(transforms):

            for k in range(i - (1 == index) * 1):
                spiral.append(list(map(sum, list(zip(spiral[-1], values)))))

    distance = max(list(map(abs, list(map(sub, *[spiral[last_num], spiral[first_num]])))))
    print("shortest distance of the two nodes is :", distance - 1)

first_num = int(input("Enter the first num :"))
last_num = int(input("Enter the last num :"))

is_spiral(first_num, last_num)
