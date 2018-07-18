# def first_perfect_square(lst):
#     l = list(enumerate(lst))
#     if l == [] or l[0][1] < 0:
#         return -1
#     else:
#         temp = int(l[0][1]**0.5)
#         if temp**2 == l[0][1]:
#             return l[0][0]
#         else:
#             return first_perfect_square(lst[1:])
#
# print(first_perfect_square([2,4,6,8,10,12]))
# print(first_perfect_square([42]))


# def first_perfect_square(numbers):
#     for i in range(0, len(numbers)):
#         if numbers[i] >= 0:
#             if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
#                 return i
#     return -1


# def num_perfect_squares(numbers):
#     cnt=0
#     for i in range(0, len(numbers)):
#         if numbers[i] >= 0:
#             if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
#                 cnt += 1
#     return cnt
#
# print(num_perfect_squares([4]*10))

# def second_largest(values):
#     max=values[0]
#     smax=values[0]
#     for val in values:
#         if val > max:
#             smax = max
#             max = val
#         elif val > smax:
#             smax = val
#
#     return smax
#
# print(second_largest([3,-2,10,-1,5]))
# print(second_largest([-2,1,1,-3,5]))
# print(second_largest(['alpha','gamma','beta','delta']))
# print(second_largest([True,False,False,True]))
# print(second_largest([3.1,3.1]))


# print french for the numbers between lo and hi (inclusive)
def print_french(lo, hi):




    return None


def digit(num, pos):
    return (num // 10 ** (pos - 1)) % 10


def num_in_french(num):  # assumes 0 <= num <= 100

    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
                 "treize",
                 "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt",
                 "quatre-vingt"]

    # Part 1: get the ones and tens digits of num
    one_digit= digit(num,1)
    ten_digit= digit(num,2)
    hun_digit= digit(num,3)

    result_str=''
    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    if hun_digit != '':
        result_str = 'cent'
    elif ten_digit == '' or (ten_digit == 1 and one_digit < 7): # 0~16
        result_str = ones_list[one_digit]
    else:
        if ten_digit >= 8:
            result_str = tens_list[ten_digit]
            if one_digit == 0:
                result_str += 's'
            elif ten_digit*10 + one_digit > 96:
                result_str += tens_list[1] +'-'+ ones_list[one_digit]
            else:
                result_str += '-' + ones_list[one_digit]
        else:
            pass


    return result_str
    # Part 4: case when the numbers are 70, 71, 72, ..., 79 and 90, 91, 92, ..., 99

    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...

    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...

    # Part 7: everything else, the most general case for 22, 23, ..., 29, 32, 33, ..., 39, 42, ...


num_in_french(80)