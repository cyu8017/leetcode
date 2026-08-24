// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

class Solution {
    var n = 0
    var k = 0
    lateinit var position: IntArray
    lateinit var prefix: IntArray
    lateinit var memo: HashMap<String, Long>
    companion object { const val INF = 1e18.toLong() }

    fun minTravelTime(l: Int, n: Int, k: Int, position: IntArray, time: IntArray): Int {
        this.n = n
        this.k = k
        this.position = position
        prefix = IntArray(n)
        prefix[0] = time[0]
        for (i in 1 until n) prefix[i] = prefix[i - 1] + time[i]
        memo = HashMap()
        return dp(0, k, 0).toInt()
    }

    fun dp(i: Int, skips: Int, last: Int): Long {
        if (i == n - 1) return if (skips == 0) 0 else INF
        val key = "$i,$skips,$last"
        memo[key]?.let { return it }
        var rate = prefix[i]
        if (last > 0) rate -= prefix[last - 1]
        var res = INF
        var end = n - 1
        if (i + skips + 1 < end) end = i + skips + 1
        for (j in i + 1..end) {
            val cand = 1L * (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1)
            if (cand < res) res = cand
        }
        memo[key] = res
        return res
    }
}
