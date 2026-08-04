// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution {
    fun shortestDistanceColor(colors: IntArray, queries: Array<IntArray>): List<Int> {
        val pos = mutableMapOf<Int, MutableList<Int>>()
        for (i in colors.indices) {
            pos.getOrPut(colors[i]) { mutableListOf() }.add(i)
        }
        val ans = mutableListOf<Int>()
        for (q in queries) {
            val i = q[0]
            val c = q[1]
            val arr = pos[c]
            if (arr == null) {
                ans.add(-1)
                continue
            }
            var lo = 0
            var hi = arr.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (arr[mid] < i) lo = mid + 1 else hi = mid
            }
            var best = Int.MAX_VALUE
            if (lo < arr.size) best = minOf(best, arr[lo] - i)
            if (lo > 0) best = minOf(best, i - arr[lo - 1])
            ans.add(if (best == Int.MAX_VALUE) -1 else best)
        }
        return ans
    }
}
