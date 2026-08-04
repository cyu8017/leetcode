// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution {
    fun earliestAcq(logs: Array<IntArray>, n: Int): Int {
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            var cur = x
            while (parent[cur] != cur) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        fun union(a: Int, b: Int): Boolean {
            val ra = find(a)
            val rb = find(b)
            if (ra == rb) return false
            parent[rb] = ra
            return true
        }
        logs.sortBy { it[0] }
        var components = n
        for (log in logs) {
            if (union(log[1], log[2])) {
                components--
                if (components == 1) return log[0]
            }
        }
        return -1
    }
}
