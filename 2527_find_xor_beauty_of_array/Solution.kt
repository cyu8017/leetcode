// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution {
    fun xorBeauty(nums: IntArray): Int {
        var ans = 0
        for (x in nums) { ans ^= x }
        return ans
    }
}
