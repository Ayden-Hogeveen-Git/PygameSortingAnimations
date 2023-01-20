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
    def __init__(self, arr):
        self.arr = arr

    def merge(self, arr1, arr2):
        """
        Merges values from 2 lists together into created list of arr1 + arr2 values
        - avoids using .pop(0) which requires O(n) time to shift values
        :param arr1: arr (half of arr)
        :param arr2: arr (other half of arr)
        :return: arr (sorted list)
        """
        arr = []
        for i in range(len(arr1) + len(arr2)):
            arr.append(0)
        index = 0  # for parsing arr
        i = 0  # for parsing arr1
        j = 0  # for parsing arr2

        # Both lists have values
        while i < len(arr1) and j < len(arr2):
            # Adds smallest value from each list
            if arr1[i] < arr2[j]:
                arr[index] = arr1[i]
                i += 1
                index += 1
            else:
                arr[index] = arr2[j]
                j += 1
                index += 1
        # arr1 has values
        while i < len(arr1):
            arr[index] = arr1[i]
            i += 1
            index += 1
        # arr2 has values
        while j < len(arr2):
            arr[index] = arr2[j]
            j += 1
            index += 1

        # print(arr)

        return arr

    def mergeSortHelper(self, arr):
        """
        Sorts the given list by dividing each list down to a trivially sorted list
        :param arr: arr (part of the list)
        :return: arr (sorted part of the list)
        """
        n = len(arr)
        if n <= 1:
            return arr

        arr1 = self.mergeSortHelper(arr[:n // 2])
        arr2 = self.mergeSortHelper(arr[n // 2:])

        return self.merge(arr1, arr2)

    def sort(self):
        """
        Sorts the given list by dividing each list down to a trivially sorted list
        :return: arr (sorted list
        """
        return self.mergeSortHelper(self.arr)
