// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

import java.util.PriorityQueue

class Solution {
    fun resultsArray(queries: Array<IntArray>, k: Int): IntArray {
        val h = PriorityQueue<Int>(compareByDescending { it })
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val d = kotlin.math.abs(queries[i][0]) + kotlin.math.abs(queries[i][1])
            h.offer(d)
            if (h.size > k) h.poll()
            ans[i] = if (h.size < k) -1 else h.peek()
        }
        return ans
    }
}
