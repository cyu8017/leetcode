// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum_cost_to_merge_sorted_lists/

class Solution {
    fun minMergeCost(lists: Array<IntArray>): Long {
        val m = lists.size
        val totalMasks = 1 shl m
        val merged = Array(totalMasks) { ArrayList<Int>() }
        val length = IntArray(totalMasks)
        val median = IntArray(totalMasks)
        for (mask in 1 until totalMasks) {
            val bit = mask and -mask
            val index = Integer.numberOfTrailingZeros(bit)
            val previous = merged[mask xor bit]
            val current = lists[index]
            val out = ArrayList<Int>(previous.size + current.size)
            var i = 0
            var j = 0
            while (i < previous.size || j < current.size) {
                if (j == current.size || (i < previous.size && previous[i] <= current[j])) {
                    out.add(previous[i++])
                } else {
                    out.add(current[j++])
                }
            }
            merged[mask] = out
            length[mask] = out.size
            median[mask] = out[(out.size - 1) / 2]
        }
        val INF = 1L shl 62
        val dp = LongArray(totalMasks)
        for (mask in 1 until totalMasks) {
            if ((mask and (mask - 1)) == 0) continue
            dp[mask] = INF
            val firstBit = mask and -mask
            var left = (mask - 1) and mask
            while (left > 0) {
                if ((left and firstBit) != 0) {
                    val right = mask xor left
                    if (right != 0) {
                        var diff = median[left] - median[right]
                        if (diff < 0) diff = -diff
                        val candidate = dp[left] + dp[right] + length[mask] + diff
                        if (candidate < dp[mask]) dp[mask] = candidate
                    }
                }
                left = (left - 1) and mask
            }
        }
        return dp[totalMasks - 1]
    }
}
