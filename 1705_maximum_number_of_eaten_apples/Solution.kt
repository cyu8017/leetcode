// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

import java.util.PriorityQueue

class Solution {
    fun eatenApples(apples: IntArray, days: IntArray): Int {
        val heap = PriorityQueue<IntArray>(compareBy { it[0] })
        val n = apples.size
        var day = 0
        var eaten = 0
        while (day < n || heap.isNotEmpty()) {
            if (day < n && apples[day] > 0) {
                heap.offer(intArrayOf(day + days[day], apples[day]))
            }
            while (heap.isNotEmpty() && heap.peek()[0] <= day) {
                heap.poll()
            }
            if (heap.isNotEmpty()) {
                val top = heap.poll()
                eaten++
                if (top[1] > 1) {
                    heap.offer(intArrayOf(top[0], top[1] - 1))
                }
            }
            day++
        }
        return eaten
    }
}
