// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution {
    fun leftmostBuildingQueries(heights: IntArray, queries: Array<IntArray>): IntArray {
        val qn = queries.size
        val ans = IntArray(qn) { -1 }
        val buckets = Array(heights.size) { ArrayList<IntArray>() }
        for (qi in 0 until qn) {
            var a = queries[qi][0]
            var b = queries[qi][1]
            if (a > b) {
                val t = a; a = b; b = t
            }
            if (a == b || heights[a] < heights[b]) {
                ans[qi] = b
                continue
            }
            buckets[b].add(intArrayOf(heights[a], qi))
        }
        val st = ArrayList<IntArray>()
        for (i in heights.size - 1 downTo 0) {
            for (p in buckets[i]) {
                val h = p[0]
                val qi = p[1]
                var lo = 0
                var hi = st.size - 1
                var pos = -1
                while (lo <= hi) {
                    val mid = (lo + hi) / 2
                    if (st[mid][0] > h) {
                        pos = st[mid][1]
                        lo = mid + 1
                    } else hi = mid - 1
                }
                ans[qi] = pos
            }
            while (st.isNotEmpty() && st[st.size - 1][0] <= heights[i]) st.removeAt(st.size - 1)
            st.add(intArrayOf(heights[i], i))
        }
        return ans
    }
}
