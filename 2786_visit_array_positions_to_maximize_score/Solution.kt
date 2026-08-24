// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    fun maxScore(nums: IntArray, x: Int): Long {
        var NEG = -(1L  shl  60)
        var even = nums[0]
        var odd = nums[0]
        if (nums[0] % 2 == 0) odd = NEG
        else even = NEG
        for (i in 1 until nums.size) {
            var v = nums[i]
            if (nums[i] % 2 == 0) even = maxOf(even + v, odd + v - x)
            else odd = maxOf(odd + v, even + v - x)
        }
        return maxOf(even, odd)
    }
}
