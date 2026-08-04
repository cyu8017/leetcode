// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import java.util.PriorityQueue

class Solution {
    fun maxEvents(events: Array<IntArray>): Int {
        events.sortBy { it[0] }
        val pq = PriorityQueue<Int>()
        var i = 0
        var ans = 0
        var day = 0
        val n = events.size
        while (i < n || pq.isNotEmpty()) {
            if (pq.isEmpty()) day = maxOf(day, events[i][0])
            while (i < n && events[i][0] <= day) {
                pq.offer(events[i][1])
                i++
            }
            while (pq.isNotEmpty() && pq.peek() < day) pq.poll()
            if (pq.isNotEmpty()) {
                pq.poll()
                ans++
                day++
            }
        }
        return ans
    }
}
