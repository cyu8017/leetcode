// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution {
    func findDifference(_ nums1: [Int], _ nums2: [Int]) -> [[Int]] {
        let s1 = Set(nums1)
        let s2 = Set(nums2)
        return [Array(s1.subtracting(s2)), Array(s2.subtracting(s1))]
    }
}
