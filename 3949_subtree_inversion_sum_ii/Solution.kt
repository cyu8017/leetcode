// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

class Solution {
    fun maxSubtreeInversionSum(edges: Array<IntArray>, nums: IntArray, k: Int): Long {
        val n = nums.size
        val graph = Array(n) { ArrayList<Int>() }
        for (edge in edges) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }
        val parent = IntArray(n) { -2 }
        parent[0] = -1
        val order = ArrayList<Int>()
        order.add(0)
        var oi = 0
        while (oi < order.size) {
            val u = order[oi]
            for (v in graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u
                    order.add(v)
                }
            }
            oi++
        }
        val infinity = 1L shl 60
        val maximum = arrayOfNulls<LongArray>(n)
        val minimum = arrayOfNulls<LongArray>(n)
        for (idx in n - 1 downTo 0) {
            val u = order[idx]
            var currentMax = LongArray(k + 1) { -infinity }
            var currentMin = LongArray(k + 1) { infinity }
            currentMax[k] = nums[u].toLong()
            currentMin[k] = nums[u].toLong()
            for (v in graph[u]) {
                if (parent[v] != u) continue
                val nextMax = LongArray(k + 1) { -infinity }
                val nextMin = LongArray(k + 1) { infinity }
                for (first in 0..k) {
                    if (currentMax[first] == -infinity) continue
                    for (childDistance in 0..k) {
                        if (maximum[v]!![childDistance] == -infinity) continue
                        var second = childDistance + 1
                        if (second > k) second = k
                        if (first < k && second < k && first + second < k) continue
                        val distance = minOf(first, second)
                        val maxValue = currentMax[first] + maximum[v]!![childDistance]
                        val minValue = currentMin[first] + minimum[v]!![childDistance]
                        nextMax[distance] = maxOf(nextMax[distance], maxValue)
                        nextMin[distance] = minOf(nextMin[distance], minValue)
                    }
                }
                currentMax = nextMax
                currentMin = nextMin
            }
            if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k]
            if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k]
            maximum[u] = currentMax
            minimum[u] = currentMin
        }
        var answer = -(1L shl 60)
        for (value in maximum[0]!!) answer = maxOf(answer, value)
        return answer
    }
}
