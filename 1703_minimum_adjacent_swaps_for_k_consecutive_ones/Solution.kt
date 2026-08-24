// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution {
    fun minMoves(nums: IntArray, k: Int): Int {
        val adjusted = ArrayList<Long>()
        for (i in nums.indices) {
            if (nums[i] == 1) {
                adjusted.add((i - adjusted.size).toLong())
            }
        }
        val m = adjusted.size
        val prefix = LongArray(m + 1)
        for (i in 0 until m) {
            prefix[i + 1] = prefix[i] + adjusted[i]
        }
        var best = Long.MAX_VALUE
        for (left in 0..(m - k)) {
            val right = left + k
            val mid = left + k / 2
            val median = adjusted[mid]
            var cost = median * (mid - left) - (prefix[mid] - prefix[left])
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1)
            best = minOf(best, cost)
        }
        return best.toInt()
    }
}
