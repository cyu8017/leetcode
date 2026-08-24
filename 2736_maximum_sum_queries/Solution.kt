// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
    fun maximumSumQueries(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums1.size
        val pts = Array(n) { IntArray(3) }
        for (i in 0 until n) {
            pts[i][0] = nums1[i]
            pts[i][1] = nums2[i]
            pts[i][2] = nums1[i] + nums2[i]
        }
        pts.sortWith(compareByDescending { it[0] })
        val qs = Array(queries.size) { IntArray(3) }
        for (i in queries.indices) {
            qs[i][0] = queries[i][0]
            qs[i][1] = queries[i][1]
            qs[i][2] = i
        }
        qs.sortWith(compareByDescending { it[0] })
        val ys = ArrayList<Int>()
        for (y in nums2) ys.add(y)
        for (q in queries) ys.add(q[1])
        ys.sort()
        var w = 0
        for (i in ys.indices) {
            if (i == 0 || ys[i] != ys[i - 1]) {
                ys[w++] = ys[i]
            }
        }
        while (ys.size > w) ys.removeAt(ys.size - 1)
        val m = ys.size
        val bit = IntArray(m + 2) { -1 }
        val ans = IntArray(queries.size)
        var j = 0
        for (q in qs) {
            while (j < n && pts[j][0] >= q[0]) {
                update(bit, m, m - rank(ys, pts[j][1]) + 1, pts[j][2])
                j++
            }
            ans[q[2]] = query(bit, m - rank(ys, q[1]) + 1)
        }
        return ans
    }

    private fun rank(ys: MutableList<Int>, y: Int): Int {
        var lo = 0
        var hi = ys.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ys[mid] < y) lo = mid + 1 else hi = mid
        }
        return lo + 1
    }

    private fun update(bit: IntArray, m: Int, i0: Int, v: Int) {
        var i = i0
        while (i <= m) {
            bit[i] = maxOf(bit[i], v)
            i += i and -i
        }
    }

    private fun query(bit: IntArray, i0: Int): Int {
        var i = i0
        var best = -1
        while (i > 0) {
            best = maxOf(best, bit[i])
            i -= i and -i
        }
        return best
    }
}
