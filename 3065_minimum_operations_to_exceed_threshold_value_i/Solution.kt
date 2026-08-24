// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var ans = 0
        for (x in nums) { if (x < k) ans++ }
        return ans
    }
}
