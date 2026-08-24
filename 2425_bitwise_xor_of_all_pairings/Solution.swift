// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
    func xorAllNums(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var ans = 0
        if nums2.count % 2 == 1 {
            for x in nums1 { ans ^= x }
        }
        if nums1.count % 2 == 1 {
            for x in nums2 { ans ^= x }
        }
        return ans
    }
}
