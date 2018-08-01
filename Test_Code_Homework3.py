import sys
from contextlib import contextmanager
from io import StringIO


mp = __import__('ch14-A_More_Programming_Practice_1')
fn = __import__('ch14-A_More_Programming_Practice_Franch')
rp = __import__('ch14-B_More_Programming_Practice_2')


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_func_print(func, answer, *args):
    with captured_output() as (out, err):
        func(*args)
    output = out.getvalue().strip()
    output = output.split('\n')
    output = [string.rstrip() for string in output]
    output = '\n'.join(output)
    try:
        assert(output == answer)
        print('Pass! ', 'function:', func.__name__, ' args: ', *args)
    except AssertionError:
        print('##########################################################')
        print('Fail! ', 'function:', func.__name__, ' args: ', *args)
        print('The answer is ', answer, ' but your output is ', output)
        print('==========================================================')


def test_func_return(func, answer, *args):
    value = func(*args)
    try:
        assert(value == answer)
        print('Pass! ', 'function:', func.__name__, ' args: ', *args)
    except AssertionError:
        print('##########################################################')
        print('Fail! ', 'function:', func.__name__, ' args: ', *args)
        print('The answer is ', answer, ' but your output is', value)
        print('==========================================================')

def test_mp1():
    print('------------------------------------------------------------')
    print('Python More Programming Practices Test Starts')
    print('------------------------------------------------------------')

    Frenchnum = ['zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf',
                 'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf',
                 'vingt', 'vingt et un', 'vingt-deux', 'vingt-trois', 'vingt-quatre', 'vingt-cinq', 'vingt-six',
                 'vingt-sept', 'vingt-huit', 'vingt-neuf',
                 'trente', 'Trente et un', 'Trente-deux', 'Trente-trois', 'Trente-quatre', 'Trente-cinq', 'Trente-six',
                 'Trente-sept', 'Trente-huit', 'Trente-neuf',
                 'quarante', 'quarante et un', 'quarante-deux', 'quarante-trois', 'quarante-quatre', 'quarante-cinq',
                 'quarante-six', 'quarante-sept', 'quarante-huit', 'quarante-neuf',
                 'cinquante', 'cinquante et un', 'cinquante-deux', 'cinquante-trois', 'cinquante-quatre',
                 'cinquante-cinq', 'cinquante-six', 'cinquante-sept', 'cinquante-huit', 'cinquante-neuf',
                 'soixante', 'soixante et un', 'soixante-deux', 'soixante-trois', 'soixante-quatre', 'soixante-cinq',
                 'soixante-six', 'soixante-sept', 'soixante-huit', 'soixante-neuf', 'soixante-dix', 'soixante et onze',
                 'soixante-douze', 'soixante-treize', 'soixante-quatorze', 'soixante-quinze', 'soixante-seize',
                 'soixante-dix-sept', 'soixante-dix-huit', 'soixante-dix-neuf',
                 'quatre-vingts', 'quatre-vingt-un', 'quatre-vingt-deux', 'quatre-vingt-trois', 'quatre-vingt-quatre',
                 'quatre-vingt-cinq', 'quatre-vingt-six', 'quatre-vingt-sept', 'quatre-vingt-huit', 'quatre-vingt-neuf',
                 'quatre-vingt-dix', 'quatre-vingt-onze', 'quatre-vingt-douze', 'quatre-vingt-treize',
                 'quatre-vingt-quatorze', 'quatre-vingt-quinze', 'quatre-vingt-seize', 'quatre-vingt-dix-sept',
                 'quatre-vingt-dix-huit', 'quatre-vingt-dix-neuf',
                 'cent']

    #mp = __import__('hw_team4_14-A')
    #fn = __import__('hw_team4_14-A_french_numbers')
    test_func_return(mp.first_perfect_square, 0, list(range(5)))
    test_func_return(mp.first_perfect_square, 1, [2, 4, 6, 8, 19, 12])
    test_func_return(mp.first_perfect_square, 4, [6, 8, 10, 12, 9])
    test_func_return(mp.first_perfect_square, 0, [1, 1])
    test_func_return(mp.first_perfect_square, -1, [-6, 6, -2, 2, -3, 3])
    test_func_return(mp.first_perfect_square, -1, [42])
    test_func_return(mp.first_perfect_square, -1, [])
    test_func_return(mp.first_perfect_square, 0, [123456789123456789 ** 2])

    test_func_return(mp.num_perfect_square, 0, [])
    test_func_return(mp.num_perfect_square, 1, [0])
    test_func_return(mp.num_perfect_square, 2, [0, 1])
    test_func_return(mp.num_perfect_square, 4, list(range(10)))
    test_func_return(mp.num_perfect_square, 0, [3] * 10)
    test_func_return(mp.num_perfect_square, 10, [4] * 10)
    test_func_return(mp.num_perfect_square, 2, [-4, -2, 0, 2, 4])

    test_func_return(mp.second_largest, 5, [3, -2, 10, -1, 5])
    test_func_return(mp.second_largest, 1, [-2, 1, 1, -3, 5])
    test_func_return(mp.second_largest, 3, [1, 2, 3, 3])
    test_func_return(mp.second_largest, 'delta', ["alpha", "gamma", "beta", "delta"])
    test_func_return(mp.second_largest, 3.1, [3.1, 3.1])
    test_func_return(mp.second_largest, True, [True, False, False, True])
    test_func_return(mp.second_largest, False, [False, False, True])

    test_func_print(fn.print_french, "0 zero\n1 un\n2 deux\n3 trois", 0, 3)
    test_func_print(fn.print_french, "18 dix-huit\n19 dix-neuf", 18, 19)
    test_func_print(fn.print_french, "100 cent", 100, 100)
    test_func_print(fn.print_french, "12 douze\n13 treize", 12, 13)
    test_func_print(fn.print_french, "70 soixante-dix\n71 soixante et onze\n72 soixante-douze\n73 soixante-treize", 70, 73)
    test_func_print(fn.print_french, "90 quatre-vingt-dix\n91 quatre-vingt-onze\n92 quatre-vingt-douze", 90, 92)
    test_func_print(fn.print_french, "19 dix-neuf\n20 vingt", 19, 20)
    test_func_print(fn.print_french, "40 quarante", 40, 40)
    test_func_print(fn.print_french, "79 soixante-dix-neuf\n80 quatre-vingts", 79, 80)
    test_func_print(fn.print_french, "20 vingt\n21 vingt et un\n22 vingt-deux", 20, 22)
    test_func_print(fn.print_french, "51 cinquante et un", 51, 51)
    test_func_print(fn.print_french, "80 quatre-vingts\n81 quatre-vingt-un\n82 quatre-vingt-deux", 80, 82)

    for i in range(0, 101):
        if fn.num_in_french(i) != Frenchnum[i].lower():
            print('Wrong!!::', i, "/ ", fn.num_in_french(i), "/", Frenchnum[i].lower())



    pass

def test_recursion():
    print('--------------------------------------------------------------------------------------------')
    print('Python More Programming Practices 2: Recursion Problems, Set and Dictionary Test Starts')
    print('--------------------------------------------------------------------------------------------')

    #rp = __import__('hw_team4_14-B')
    #1
    test_func_return(rp.count_matches, 3, [0, 1, 0, 4, 2, 0], 0)
    test_func_return(rp.count_matches, 0, ["a", "b", "c"], 1)
    test_func_return(rp.count_matches, 0, [], "a")

    #2
    nums = [1, 2, 3]
    test_func_return(rp.double_each, [1, 1, 2, 2, 3, 3], nums)
    if nums != [1, 2, 3]:
        print("Fail!! Wrong!!")
    test_func_return(rp.double_each, [], [])

    #3
    nums = [1, 2, 3]

    test_func_return(rp.sums_to, True, nums, 6)
    test_func_return(rp.sums_to, False, nums, 5)
    test_func_return(rp.sums_to, False, [], 1)

    #4
    test_func_return(rp.is_reverse, True, "abc", "cba")
    test_func_return(rp.is_reverse, False, "abc", "abc")
    test_func_return(rp.is_reverse, False, "abc", "dcba")
    test_func_return(rp.is_reverse, False, "abc", "cb")
    test_func_return(rp.is_reverse, True, "", "")

    #5
    test_func_return(rp.sort_repeated, [1, 2], [1, 2, 3, 2, 1])
    test_func_return(rp.sort_repeated, [2], [1, 2, 3, 2, 2, 4])
    test_func_return(rp.sort_repeated, [], list(range(100)))

    #6
    test_func_return(rp.make_Dict_number, {2: 2, 3: 1, 4: 3, 5: 2, 6: 1}, [2, 5, 3, 4, 6, 4, 2, 4, 5])
    #test_func_return(rp.make_Dict_number_noget, {2: 2, 3: 1, 4: 3, 5: 2, 6: 1}, [2, 5, 3, 4, 6, 4, 2, 4, 5])
    test_func_return(rp.most_Frequent, 4, [2, 5, 3, 4, 6, 4, 2, 4, 5])

    #7
    letters = {1: "a", 2: "b", 3: "a"}
    test_func_return(rp.histogram, {'b': 1, 'a': 2}, letters)

    letters = {1: "a", 2: "b", 3: "c"}
    test_func_return(rp.histogram, {'b': 1, 'a': 1, 'c': 1}, letters)

    letters[4] = "a"
    letters[5] = "b"
    letters[6] = "a"
    test_func_return(rp.histogram, {'b': 2, 'a': 3, 'c': 1}, letters)


if __name__ == '__main__':
    test_mp1()
    test_recursion()

