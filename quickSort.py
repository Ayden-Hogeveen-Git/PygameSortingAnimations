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
    def __init__(self, arr):
        self.arr = arr
        self.first = 0
        self.last = len(arr)

    def partition(self, first, last):
        """
        Uses pointers to sort all values less than the pivot to the left, and all greater than the pivot to the right
        Then returns the location of the pivot in that case
        :param first: int (first index of the list)
        :param last: int (last index of the list)
        :return small: int (pivot location in sorted list)
        """
        pivot = self.arr[first]
        # Initializes 2 pointers, big 1 index after pivot, small at other end of list
        big = first + 1
        small = last

        # Continue until big and small cross
        while big <= small:
            # Stop when bigger than pivot
            while big <= last and self.arr[big] <= pivot:
                big += 1
            # Stop when smaller than pivot
            while self.arr[small] > pivot:
                small -= 1

            # Swap big and small
            if big < small:
                self.arr[small], self.arr[big] = self.arr[big], self.arr[small]

        # Swap pivot to final index
        self.arr[first], self.arr[small] = self.arr[small], self.arr[first]
        return small

    def sort_helper(self, first, last):
        """
        Recursive helper function to sort the list using the partition
        :param first: int (first index of the list)
        :param last: int (last index of the list)
        :return self.arr: arr (sorted list)
        """
        if first >= last:
            return self.arr
        pivotIndex = self.partition(first, last)
        # print(self.arr)
        self.sort_helper(first, pivotIndex - 1)
        self.sort_helper(pivotIndex + 1, last)
        return self.arr

    def sort(self):
        """
        Recursively sorts the list using the partition
        :return self.arr: arr (sorted list)
        """
        return self.sort_helper(0, len(self.arr) - 1)
