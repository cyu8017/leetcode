// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution {
    func arraysIntersection(_ 1: [Int], _ 2: [Int], _ 3: [Int]) -> [Int] {
        return Set(arr1).intersect(Set(arr2)).intersect(Set(arr3)).sorted()
    }
}
