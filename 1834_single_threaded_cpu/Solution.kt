// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

import java.util.PriorityQueue

class Solution {
    fun getOrder(tasks: Array<IntArray>): IntArray {
        val indexed = tasks.indices.sortedWith(compareBy({ tasks[it][0] }, { it }))
        var i = 0
        val n = tasks.size
        val heap = PriorityQueue<IntArray>(compareBy({ it[0] }, { it[1] }))
        var time = 0L
        val order = IntArray(n)
        var out = 0

        while (i < n || heap.isNotEmpty()) {
            if (i < n && heap.isEmpty()) {
                time = maxOf(time, tasks[indexed[i]][0].toLong())
            }
            while (i < n && tasks[indexed[i]][0] <= time) {
                val idx = indexed[i]
                heap.offer(intArrayOf(tasks[idx][1], idx))
                i++
            }
            val cur = heap.poll()
            time += cur[0]
            order[out++] = cur[1]
        }
        return order
    }
}
