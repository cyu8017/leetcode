// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

class Solution {
    fun highFive(items: Array<IntArray>): Array<IntArray> {
        val scores = mutableMapOf<Int, MutableList<Int>>()
        for (item in items) {
            scores.getOrPut(item[0]) { mutableListOf() }.add(item[1])
        }
        val ids = scores.keys.sorted()
        return Array(ids.size) { i ->
            val id = ids[i]
            val top = scores[id]!!.sortedDescending()
            val sum = (0 until 5).sumOf { top[it] }
            intArrayOf(id, sum / 5)
        }
    }
}
