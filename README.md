# Problems vs Algorithms

<!-- Reasoning behind decisions in the code e.g. why this data structure -->
<!-- Time and space efficiency of solution -->

## Problem 1: Finding the Square Root of any Integer

The solution has a time complexity of O(log n) and a space complexity of O(1).
This is because of the logarithmic nature to the problem. If the input number is small, only a few iterations are required to get the solution. If the input number is larger, the number of iterations required scales logarithmically.
For example; if number = 4; it would first try 0^0 = 0, then 1^1 = 1 and finally 2^2 = 4.
Finding the solution 4 < number <= 9 only takes 1 more iteration, because 4^2 = 16.

## Problem 2: Search in a Rotated Sorted Array

The solution has a time complexity of O(log n) and a space complexity of O(log n). The solution implemented is analagous to recursive binary search, a type of divide and conquer method whereby the array gets halved with each recursion. Therefore, in the worst case where the element does not exist in the array, the recursion depth will be log n.

The base case is if the mid element of the current search range equals the number being searched. To successfully half the array search size in each recursion, it is first necessary to understand if an array contains the rotated element, if not, then we know it is a regular sorted list that ascends from smallest to largest element, left to right. This means we can easily know if our number falls within this range, if so, iterate with this half of the array, otherwise recursve the other half. If the array contains a rotation, known by comparing the first and last elements of the array half, then we know the other half does not contain a rotation and we can check to see if the number falls in this non-rotated array easily as before. If it is not in there, it must be in the rotated half, so recurse this half.

## Problem 3: Search in a Rotated Sorted Array

The solution has an average time complexity of O(n logn) due to the quicksort method, which has an average space complexity is O(log n) due to the recursion depth. The overall space complexity however is O(n) due to the string addition of each element in the input array. This is also the worst case space complexity of quicksort, O(n), if a bad pivot is chosen at each recursion.

Mergesort could have also been used. This has the advantage of worst case time complexity being O(n logn) whilst quicksort has worst case O(n2) if a bad pivot is chosen at each recursion. However, the space complexity of merge sort is O(n) whilst quick-sort is an in-place sorting method, so has O(1) space complexity at each recursion. Quicksort was chosen due to the same average time complexity, if not slightly faster than mergesort, and requires less memory to run on average.

## Problem 4: Dutch National Flag Problem

The solution has a time complexity of Θ(n) and a space complexity of Θ(1). The solution sorts the array in-place in a single traversal. In-place sorting was chosen over creating a new array because the latter would increase the space complexity to Θ(n).

## Problem 5: Autocomplete with Tries

The solution has a time complexity of O(n) and a space complexity of O(n).

Finding a Trie node for a given prefix takes O(n) time, where n is the length of the prefix.
Finding the suffixes for a given prefix node then takes O(n) time, where n is the total number of characters in the trie, in the worst case when the prefix matches all words in the trie.
Each recursion into a new child TrieNode adds a frame to the recursion stack, and as every node is visited in the worst case, this causes the linear space complexity.

## Problem 6: Max and Min in an Unsorted Array

The solution has a time complexity of Θ(n) and a space complexity of Θ(1). The solution runs in a single traversal of the array. This method was chosen over the alternative, which was to build functionality to find the kth smallest element for k = 1 and k = len(array) - 1. This would be achieved through a recursive divide and conquer method. The downside to this divide and conquer method is, although it would also have a time complexity of O(n), it would go through multiple recursions to find a good pivot and the kth element. The space complexity would also be larger due to the recursive calls.

## Problem 7: HTTP Router using a Trie

The solution has a time complexity of O(n) and a space complexity of O(n), with similar reasons to Problem 5.

Adding a handler takes O(n) time in the worst case. Looking up a handler also takes O(n) time in the worst case. Here, n represents the number of sub-paths that exist within the router.

The function to split paths was incorporated within the RouteTrie class instead of the Router class so that the RouteTrie class works as intended without relying on the implementation of the Router class.
