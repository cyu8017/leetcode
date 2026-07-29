// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

import java.util.PriorityQueue

class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        val pq = PriorityQueue<Int>(compareByDescending { it })
        for (s in stones) pq.offer(s)
        while (pq.size > 1) {
            val a = pq.poll(); val b = pq.poll()
            if (a != b) pq.offer(a - b)
        }
        return if (pq.isEmpty()) 0 else pq.peek()
    }
}
