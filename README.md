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
