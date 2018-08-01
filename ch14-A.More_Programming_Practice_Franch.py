# print french for the numbers between lo and hi (inclusive)
def print_french(lo, hi):
    for i in range(lo,hi):
        print(i , num_in_french(i))
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
    if hun_digit != 0: #100
        result_str = 'cent'
    elif num < 17: # 0~16
        result_str = ones_list[num]
    else:
        if num >=70 and num < 77:
            if one_digit == 1:
                result_str += tens_list[6] + ' et ' + ones_list[num-60]
            else:
                result_str = tens_list[6] + '-' + ones_list[num-60]
        elif num >= 77 and num < 80:
            result_str = tens_list[6] + '-' + tens_list[1] + '-' + ones_list[one_digit]
        elif num >= 80:  #80이상
            result_str = tens_list[4] + '-' + tens_list[2]
            if num == 80:
                result_str += 's'
            elif num > 96:
                result_str += '-' + tens_list[1] + '-' + ones_list[num-80]
            else:
                result_str += '-' + ones_list[num-80]
        else:
            if num > 16: ## 17 ~~ 69

                if one_digit == 0:
                    result_str += tens_list[ten_digit]
                elif one_digit == 1:
                    result_str += tens_list[ten_digit] + ' et ' + ones_list[one_digit]
                else:
                    result_str += tens_list[ten_digit] + '-' + ones_list[one_digit]
            else:
                pass

    return result_str


print_french(0,101)