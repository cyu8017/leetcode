// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): IntArray {
        val pairs = Array(n) { IntArray(2) }
        for (i in 0 until n) pairs[i] = intArrayOf(nums[i], i)
        pairs.sortBy { it[0] }
        val m = 20
        val f = Array(n) { IntArray(m) }
        var r = n - 1
        for (l in n - 1 downTo 0) {
            while (pairs[r][0] - pairs[l][0] > maxDiff) r--
            val i = pairs[l][1]
            val j = pairs[r][1]
            f[i][0] = j
            for (k in 1 until m) f[i][k] = f[f[i][k - 1]][k - 1]
        }
        val ans = ArrayList<Int>()
        for (q in queries) {
            var i = q[0]
            var j = q[1]
            if (nums[i] > nums[j]) {
                val tmp = i; i = j; j = tmp
            }
            if (i == j) { ans.add(0); continue }
            if (nums[i] == nums[j]) { ans.add(1); continue }
            var d = 0
            for (k in m - 1 downTo 0) {
                if (nums[f[i][k]] < nums[j]) {
                    d = d or (1 shl k)
                    i = f[i][k]
                }
            }
            if (nums[f[i][0]] < nums[j]) ans.add(-1)
            else ans.add(d + 1)
        }
        return ans.toIntArray()
    }
}
