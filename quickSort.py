# quickSort.py
"""
title: QuickSort Algorithm
author: Ayden Hogeveen
date-created: 1/20/23
"""


class QuickSort:
    """
    QuickSort Algorithm
    Divide and Conquer
    - Finds a pivot element in the list, which divides the list into different parts
    - Uses 3 pointers, the pivot, big, and small (the pivot is the first element)
        - Can be made more efficient by choosing the "best" pivot
    - Swaps values so that the values on one side of the list are greater than the pivot value
      and the values on the other side are lesser than the pivot
    This algorithm uses recursion to bring the pivot to the proper position, so that the values on
    either side are smaller and larger, respectively, then to quickSort both parts.

    Time Complexity:
    Best Case: O(nlogn), Worst Case: O(n^2)
    Extra Space:
    O(1)

    Called "quick" sort because of the average case being O(nlogn)
    """
