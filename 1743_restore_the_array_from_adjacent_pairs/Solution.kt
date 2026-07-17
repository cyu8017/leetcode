// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution {
    fun restoreArray(adjacentPairs: Array<IntArray>): IntArray {
        val graph = HashMap<Int, MutableList<Int>>()
        for ((a, b) in adjacentPairs.map { it[0] to it[1] }) {
            graph.getOrPut(a) { mutableListOf() }.add(b)
            graph.getOrPut(b) { mutableListOf() }.add(a)
        }
        var start = 0
        for (pair in adjacentPairs) {
            if (graph.getValue(pair[0]).size == 1) {
                start = pair[0]
                break
            }
            if (graph.getValue(pair[1]).size == 1) {
                start = pair[1]
                break
            }
        }
        val n = graph.size
        val ans = IntArray(n)
        ans[0] = start
        var prev: Int? = null
        for (i in 1 until n) {
            val cur = ans[i - 1]
            val neighbors = graph.getValue(cur)
            ans[i] = if (neighbors[0] != prev) neighbors[0] else neighbors[1]
            prev = cur
        }
        return ans
    }
}
