// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

class Solution {
    fun countPairs(n: Int, edges: Array<IntArray>, queries: IntArray): IntArray {
        val deg = IntArray(n + 1)
        val shared = HashMap<Long, Int>()
        for (edge in edges) {
            val a = minOf(edge[0], edge[1])
            val b = maxOf(edge[0], edge[1])
            deg[a]++
            deg[b]++
            val key = a.toLong() * 100000 + b
            shared[key] = (shared[key] ?: 0) + 1
        }
        val sortedDeg = deg.copyOfRange(1, n + 1)
        sortedDeg.sort()
        val ans = IntArray(queries.size)
        for (qi in queries.indices) {
            val q = queries[qi]
            var res = 0
            var left = 0
            var right = n - 1
            while (left < right) {
                if (sortedDeg[left] + sortedDeg[right] > q) {
                    res += right - left
                    right--
                } else {
                    left++
                }
            }
            for ((key, count) in shared) {
                val a = (key / 100000).toInt()
                val b = (key % 100000).toInt()
                val sum = deg[a] + deg[b]
                if (sum > q && q >= sum - count) {
                    res--
                }
            }
            ans[qi] = res
        }
        return ans
    }
}
