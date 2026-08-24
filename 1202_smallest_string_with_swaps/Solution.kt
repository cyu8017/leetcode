// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import java.util.PriorityQueue

class Solution {
    fun smallestStringWithSwaps(s: String, pairs: List<List<Int>>): String {
        val n = s.length
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            var cur = x
            while (parent[cur] != cur) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        for (p in pairs) {
            val ra = find(p[0])
            val rb = find(p[1])
            parent[ra] = rb
        }
        val groups = mutableMapOf<Int, PriorityQueue<Char>>()
        for (i in 0 until n) {
            groups.getOrPut(find(i)) { PriorityQueue() }.offer(s[i])
        }
        val sb = StringBuilder()
        for (i in 0 until n) sb.append(groups[find(i)]!!.poll())
        return sb.toString()
    }
}
