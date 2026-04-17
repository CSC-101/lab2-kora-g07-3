def smallest(n:float, m:float) -> float:
    if n < m:
        return n             #calls Second
    else:
        return m

first = smallest(3, 2)       # first = 2
second = smallest(2, 2)      # seconed=2 this isn't reasonable because there is no = and yet the answer is 2
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # when a > b is true and a > c is true
    elif b > c:
        return b + c             # when a<=b or a<=c and b>c
    else:
        return 2 * c             # when a<=b or a<=c and b<=c


answer1 = function2(3, 2, 1)     # 1
answer2 = function2(2, 3, 1)     # 4
answer3 = function2(2, 1, 3)     # 6
print()

a_value = 10
another = 20
t = a_value
a_value = another
another = t



def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # First=false, second=True
    if test:                            # Is preventing a false from rentunring L[indx]
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # None
second = checked_access([1, 0, 1], 2)    #1
print()


def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    #this calls first, and adding "4" + "2" + "3"
    elif len(L) > 1:                                  #  This applies to third
        result = len(L[0]) + len(L[1])                # this adds "7" + "4"
    elif len(L) > 0:                                  # applies to second
        result = len(L[0])                            # =11
    else:                                             # doesnt apply
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"]) #=9
second = length_sum(["second call"]) #= 11
third = length_sum(["another", "call"])
print()


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH']
         # first=['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.'], second=['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
         # because L was re-written in the second performance of the function and first is an alias for L both L and second are the same.
print(first)
