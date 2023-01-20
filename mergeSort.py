# mergeSort.py
"""
title: MergeSort Algorithm
author: Ayden Hogeveen
date-created: 1/20/23
"""


class MergeSort:
    """
    MergeSort Algorithm
    Another Divide and Conquer Algorithm
    Split the list in half, until reaching the base case (a sorted list -- a list of 1 element is trivially
    sorted), then merge these sorted lists by comparing the lowest number in each list, until reaching a
    fully sorted list.

    Time Complexity:
    Best Case: O(nlogn), Worst Case: O(nlogn)
    Extra Space:
    O(n)
    """
