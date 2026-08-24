// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var xorr = 0
        for (v in nums) { xorr ^= v }
        var diff = xorr ^ k
        var ans = 0
        while (diff > 0) {
            ans += diff & 1
            diff >>= 1
        }
        return ans
    }
}
