// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

class Solution {
    private var prefix: LongArray? = null
    private var previous: LongArray? = null
    private var current: LongArray? = null
    private val INF: Long = 1L  shl  62

    fun minPartitionScore(nums: IntArray, k: Int): Long {
        var n = nums.size
        prefix = LongArray(n + 1)
        for (i in 0 until n) { prefix[i + 1] = prefix[i] + nums[i] }
        previous = LongArray(n + 1)
        previous.fill(INF)
        previous[0] = 0
        for (parts in 1..k) {
            current = LongArray(n + 1)
            current.fill(INF)
            compute(parts, n, parts - 1, n - 1)
            previous = current
        }
        return previous[n]
    }

    private fun value(left: Int, right: Int): Long {
        var sum = prefix[right] - prefix[left]
        return sum * (sum + 1) / 2
    }

    private fun compute(lo: Int, hi: Int, optLo: Int, optHi: Int) {
        if (lo > hi) return
        var mid = (lo + hi) / 2
        var bestIndex = -1
        var end = minOf(optHi, mid - 1)
        for (split in optLo..end) {
            if (previous[split] == INF) continue
            var candidate = previous[split] + value(split, mid)
            if (candidate < current[mid]) {
                current[mid] = candidate
                bestIndex = split
            }
        }
        if (bestIndex == -1) bestIndex = optLo
        compute(lo, mid - 1, optLo, bestIndex)
        compute(mid + 1, hi, bestIndex, optHi)
    }
}
