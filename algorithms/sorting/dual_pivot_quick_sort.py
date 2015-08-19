"""
    dual_pivot_quick_sort.py
    Implementation of dual-pivot quick sort on a seq and returns a sorted seq.
    In-place version.

    Dual-pivot Quick Sort Overview:
    ------------------------------------
    Use two pivots(p1,p2, p1 <= p2) to divide list into 3 parts: partI < p1, p1 <= partII <= p2, partIII > p2
    |   |        |   |               |   |               |    |         |   |
    | p1| <p1    | h | p1 <= & <= p2 | k |       ?       | l  | > p2    | p2|
    |   | part I |     part II       |         part IV        | part III|   |
    Time Complexity: O(n**2) worst case()
    Space Complexity: O(1)
    Stable: No
"""
def dual_pivot_quick_sort(seq, p1, p2):
    if p2 <= p1:
        return seq
    k = p1+1
    h = k
    l = p2-1
    if seq[p1] > seq[p2]:
        seq[p1], seq[p2] = seq[p2], seq[p1]
    while k <= l:
    #l is the last element of part IV, where all elements have not checked yet
        if seq[k] < seq[p1]:
            seq[h], seq[k] = seq[k], seq[h]
            #h is the first element of part II
            h += 1 #increase h by 1, for pointing to the first element of part II
            k += 1 #increase k by 1, because we have checked seq[k]
        elif seq[k] > seq[p2]:
            seq[k], seq[l] = seq[l], seq[k]
            l -= 1
            #don't increase k, as we have not check the new value of seq[k] yet
        else: k += 1 # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1
    l += 1
    seq[p1], seq[h] = seq[h], seq[p1]
    seq[p2], seq[l] = seq[l], seq[p2]
    dual_pivot_quick_sort(seq, p1, h-1)
    dual_pivot_quick_sort(seq, h+1, l-1)
    dual_pivot_quick_sort(seq, l+1, p2)
    return seq



