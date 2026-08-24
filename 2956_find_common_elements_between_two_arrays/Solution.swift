// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution {
    func findIntersectionValues(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let s1 = Set(nums1), s2 = Set(nums2)
        let a = nums1.filter { s2.contains($0) }.count
        let b = nums2.filter { s1.contains($0) }.count
        return [a, b]
    }
}
