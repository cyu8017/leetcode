// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    func uniformArray(_ nums1: [Int]) -> Bool {
        var mn = Int.max
        for x in nums1 {
            if x % 2 == 1 && x < mn { mn = x }
        }
        for x in nums1 {
            if x % 2 == 0 && mn != Int.max && x < mn { return false }
        }
        return true
    }
}
