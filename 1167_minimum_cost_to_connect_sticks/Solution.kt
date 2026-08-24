// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import java.util.PriorityQueue

class Solution {
    fun connectSticks(sticks: IntArray): Int {
        if (sticks.size <= 1) return 0
        val pq = PriorityQueue<Int>()
        for (s in sticks) pq.offer(s)
        var ans = 0
        while (pq.size > 1) {
            val cost = pq.poll() + pq.poll()
            ans += cost
            pq.offer(cost)
        }
        return ans
    }
}
