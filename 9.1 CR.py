"""
9.1CR task
Student ID 537318
Haris Liang
list

"""


def displayAndCountOddsAndEvens(number):
    odd_numbers_arr = []
    even_numbers_arr = []

    print("The list is : ", number)

    for i in number:
        if i % 2 == 1:
            odd_numbers_arr.append(i)
        else:
            even_numbers_arr.append(i)

    if odd_numbers_arr:  # when an arr is empty, this arr == false
        print("Odd numbers:")
        for ii in odd_numbers_arr:
            print(ii)
    else:
        pass

    if even_numbers_arr:  # when an arr is empty, this arr == false
        print("Even numbers:")
        for ii in even_numbers_arr:
            print(ii)
    else:
        pass

    odd_num = len(odd_numbers_arr)
    even_num = len(even_numbers_arr)
    print("There were %d odds and %d evens" % (odd_num, even_num))
    print("")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # arr
displayAndCountOddsAndEvens(list)

list2 = [2, 4, 6, 8, 10]
displayAndCountOddsAndEvens(list2)

list3 = [1, 3, 5, 7, 9]
displayAndCountOddsAndEvens(list3)

list4 = []
displayAndCountOddsAndEvens(list4)
