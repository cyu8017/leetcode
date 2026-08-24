// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution {
    fun minSwaps(nums: IntArray): Int {
        var ones: Int = 0
        for (x in nums) ones += x
        if (ones == 0) return 0
        var n: Int = nums.size, window = 0
        for (i in 0 until ones) window += nums[i]
        var best: Int = window
        for (i in 0 until n) {
            window -= nums[i]
            window += nums[(i + ones) % n]
            best = maxOf(best, window)
        }
        return ones - best
    }
}
