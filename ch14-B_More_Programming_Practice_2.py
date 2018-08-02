def count_matches(some_list, value):
    if some_list == []:
        return 0
    else:
        if some_list[0] == value:
            return 1 + count_matches(some_list[1:],value)
        else:
            return count_matches(some_list[1:],value)

def double_each(some_list):
    if some_list == []:
        return []
    else:
        return [some_list[0]]*2 + double_each(some_list[1:])

def sums_to(nums, k):
    if nums == []:
        if k ==0 : return True
        else: return False
    else:
        k = k - nums[0]
        return sums_to(nums[1:],k)

def is_reverse(string1, string2):
    if string1 == '' and string2 == '':
        return True
    elif string1 == '' or string2 == '':
        return False
    elif string1[0] != string2[-1]:
        return False
    else:
        return is_reverse(string1[1:],string2[:-1])


def sort_repeated(L):
    L = sorted(L)
    rslt=[]
    for i in range(0,len(L)):
        if i+1 < len(L):
            if L[i] == L[i+1]: rslt.append(L[i])

    return list(set(rslt))

def make_Dict_number(lst):
    lst = sorted(lst)
    dict ={}
    for i in lst:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict

def make_Dict_number_get(lst):
    lst = sorted(lst)
    dict ={}
    for i in lst:
        dict[i] = 1 + dict.get(i,0)

    return dict

def most_Frequent(lst):
    dict = {}
    for i in lst:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    ret = sorted(dict.items(), key=lambda x:x[1], reverse=True)[0][0]
    return ret

def mostFrequent_get(lst):
    dict = {}
    for i in lst:
        dict[i] = 1 + dict.get(i, 0)

    return sorted(dict.items(), key=lambda x:x[1], reverse=True)[0][0]

def histogram(d):
    dict={}

    for v in d.values():
        if v in dict:
            dict[v] += 1
        else:
            dict[v] = 1

    return dict
