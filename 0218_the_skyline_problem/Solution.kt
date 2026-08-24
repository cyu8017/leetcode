// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

import java.util.PriorityQueue

class Solution {
    fun getSkyline(buildings: Array<IntArray>): List<List<Int>> {
        val events = mutableListOf<IntArray>()
        for ((left, right, height) in buildings.map { Triple(it[0], it[1], it[2]) }) {
            events.add(intArrayOf(left, -height, right))
            events.add(intArrayOf(right, 0, 0))
        }
        events.sortWith(compareBy({ it[0] }, { it[1] }))

        val result = mutableListOf<List<Int>>()
        val live = PriorityQueue<IntArray>(compareBy { it[0] })
        live.offer(intArrayOf(0, Int.MAX_VALUE))

        for ((x, negH, end) in events.map { Triple(it[0], it[1], it[2]) }) {
            while (live.peek()[1] <= x) {
                live.poll()
            }
            if (negH != 0) {
                live.offer(intArrayOf(negH, end))
            }
            val height = -live.peek()[0]
            if (result.isEmpty() || result.last()[1] != height) {
                result.add(listOf(x, height))
            }
        }
        return result
    }
}
