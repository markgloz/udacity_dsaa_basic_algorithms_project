# Problems vs Algorithms

## Problem 1: Finding the Square Root of any Integer

The solution has a time complexity of O(log n) and a space complexity of O(1).
This is because of the logarithmic nature to the problem. If the input number is small, only a few iterations are required to get the solution. If the input number is larger, the number of iterations required scales logarithmically.
For example; if number = 4; it would first try 0^0 = 0, then 1^1 = 1 and finally 2^2 = 4.
Finding the solution 4 < number <= 9 only takes 1 more iteration, because 4^2 = 16.

<!-- Reasoning behind decisions in the code e.g. why this data structure -->
<!-- Time and space efficiency of solution -->

## Problem 2: Search in a Rotated Sorted Array
