// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

class Solution {
    class FenwickMax(n: Int) {
        private val vals = IntArray(n + 1)
        fun maximize(i0: Int, `val`: Int) {
            var i = i0
            while (i < vals.size) {
                vals[i] = maxOf(vals[i], `val`)
                i += i and -i
            }
        }
        fun get(i0: Int): Int {
            var i = i0
            var res = 0
            while (i > 0) {
                res = maxOf(res, vals[i])
                i -= i and -i
            }
            return res
        }
    }

    private fun lowerBound(a: MutableList<Int>, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    fun getResults(queries: Array<IntArray>): BooleanArray {
        var n = queries.size * 3
        if (n > 50000) n = 50000
        val tree = FenwickMax(n + 1)
        val obs = ArrayList<Int>()
        obs.add(0)
        obs.add(n)
        for (q in queries) {
            if (q[0] == 1) {
                val x = q[1]
                val idx = lowerBound(obs, x)
                if (idx == obs.size || obs[idx] != x) obs.add(idx, x)
            }
        }
        for (i in 0 until obs.size - 1) {
            tree.maximize(obs[i + 1], obs[i + 1] - obs[i])
        }
        val ans = ArrayList<Boolean>()
        for (i in queries.size - 1 downTo 0) {
            val typ = queries[i][0]
            val x = queries[i][1]
            if (typ == 1) {
                val j = lowerBound(obs, x)
                val prev = obs[j - 1]
                val next = obs[j + 1]
                obs.removeAt(j)
                tree.maximize(next, next - prev)
            } else {
                val sz = queries[i][2]
                val j = lowerBound(obs, x + 1) - 1
                val prev = obs[j]
                ans.add(tree.get(prev) >= sz || x - prev >= sz)
            }
        }
        ans.reverse()
        return BooleanArray(ans.size) { ans[it] }
    }
}
