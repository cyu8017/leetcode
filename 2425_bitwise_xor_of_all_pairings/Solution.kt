// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
    fun xorAllNums(nums1: IntArray, nums2: IntArray): Int {
            var ans: Int = 0
            if (nums2.size % 2 == 1) {
                for (x in nums1) ans ^= x
            }
            if (nums1.size % 2 == 1) {
                for (x in nums2) ans ^= x
            }
            return ans
    }
}
