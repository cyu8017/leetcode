// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution {
    fun minLengthAfterRemovals(nums: List<Int>): Int {
        val n = nums.size
        var mx = 0
        val freq = HashMap<Int, Int>()
        for (v in nums) {
            val c = freq.getOrDefault(v, 0) + 1
            freq[v] = c
            mx = maxOf(mx, c)
        }
        if (mx <= n / 2) return n % 2
        return 2 * mx - n
    }
}
