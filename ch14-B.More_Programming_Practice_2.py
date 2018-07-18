# def count_matches(some_list, value):
#     if some_list == []:
#         return 0
#     else:
#         if some_list[0] == value:
#             return 1 + count_matches(some_list[1:],value)
#         else:
#             return count_matches(some_list[1:],value)
#
# a = count_matches([0,1,0,4,2,0],0)
# print(a)
# a = count_matches(['a','b','c'],1)
# print(a)
# a = count_matches([],'a')
# print(a)

# def double_each(some_list):
#     if some_list == []:
#         return []
#     else:
#         return [some_list[0]]*2 + double_each(some_list[1:])
#
# nums = [1,2,3]
# a = double_each(nums)
# print(a)
# print(nums)
# print(double_each([]))

# def sums_to(nums, k):
#     if nums == []:
#         if k ==0 : return True
#         else: return False
#     else:
#         k = k - nums[0]
#         return sums_to(nums[1:],k)
#
# nums=[]
# a = sums_to(nums, 1)
# print(a)

# def is_reverse(string1, string2):
#     if string1 == '' and string2 == '':
#         return True
#     elif string1 == '' or string2 == '':
#         return False
#     elif string1[0] != string2[-1]:
#         return False
#     else:
#         return is_reverse(string1[1:],string2[:-1])
#
# a = is_reverse('abc','cba')
# print(a)
# a = is_reverse('abc','abc')
# print(a)
# a = is_reverse('abc','dcba')
# print(a)
# a = is_reverse('abc','cb')
# print(a)
# a = is_reverse('','')
# print(a)


# def sort_repeated(L):
#     L = sorted(L)
#     rslt=[]
#     for i in range(0,len(L)):
#         if i+1 < len(L):
#             if L[i] == L[i+1]: rslt.append(L[i])
#
#     return list(set(rslt))
#
# a = sort_repeated([1,2,3,2,1])
# print(a)
# a = sort_repeated([1,2,3,2,2,4])
# print(a)
# a = sort_repeated(list(range(100)))
# print(a)


# def sort_repeated(L):
#     seen = set()
#     seenAgain = set()
#     for element in L:
#         if element in seen:
#             seenAgain.add(element)
#         seen.add(element)
#     return sorted(seenAgain)