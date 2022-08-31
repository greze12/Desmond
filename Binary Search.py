#o(log(n)) time | o(log(n)) space
# Sorted
#To find the target value in a list, if target found = left<right else: left>right, l=o, r=len(list)-1

def binarysearch(array, target):
    return binarysearchhelper(array, target, 0, len(array)-1)
def binarysearchhelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    Match = array(mid)
    if target == Match:
        return mid
    elif target < Match:
        return binarysearchhelper(array , target, left, mid-1)
    else:
        return binarysearchhelper(array , target, mid+1, right)


   
