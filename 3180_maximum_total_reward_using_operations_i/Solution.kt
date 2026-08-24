// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

class Solution {
    private lateinit var rewardValues: IntArray
    private lateinit var f: IntArray
    private var n = 0

    fun maxTotalReward(rewardValues: IntArray): Int {
        rewardValues.sort()
        this.rewardValues = rewardValues
        n = rewardValues.size
        f = IntArray(rewardValues[n - 1] shl 1) { -1 }
        return dfs(0)
    }

    private fun dfs(x: Int): Int {
        if (f[x] != -1) return f[x]
        val idx = upperBound(rewardValues, x)
        f[x] = 0
        for (it in idx until n) {
            f[x] = maxOf(f[x], rewardValues[it] + dfs(x + rewardValues[it]))
        }
        return f[x]
    }

    private fun upperBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] <= x) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
