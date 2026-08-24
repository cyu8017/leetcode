// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution {
    fun arraysIntersection(arr1: IntArray, arr2: IntArray, arr3: IntArray): List<Int> {
        return arr1.toSet().intersect(arr2.toSet()).intersect(arr3.toSet()).sorted()
    }
}
