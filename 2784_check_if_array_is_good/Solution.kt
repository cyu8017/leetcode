// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    fun isGood(nums: IntArray): Boolean {
        var n = nums.size - 1
        if (n < 1) return false
        var freq = IntArray(n + 1)
        for (v in nums) {
            if (v < 1 || v > n) return false
            freq[v]++
        }
        for (i in 1 until n) { if (freq[i] != 1) return false }
        return freq[n] == 2
    }
}
