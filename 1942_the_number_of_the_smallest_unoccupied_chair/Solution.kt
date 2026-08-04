// LeetCode 1942
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import java.util.PriorityQueue

class Solution {
    fun smallestChair(times: Array<IntArray>, targetFriend: Int): Int {
        val order = times.indices.sortedBy { times[it][0] }
        val free = PriorityQueue<Int>()
        var nextChair = 0
        val leaving = PriorityQueue<IntArray>(compareBy { it[0] })
        for (i in order) {
            val arr = times[i][0]
            val leave = times[i][1]
            while (leaving.isNotEmpty() && leaving.peek()[0] <= arr) free.add(leaving.poll()[1])
            val chair = if (free.isNotEmpty()) free.poll() else nextChair++
            if (i == targetFriend) return chair
            leaving.add(intArrayOf(leave, chair))
        }
        return -1
    }
}
