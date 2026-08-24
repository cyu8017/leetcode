// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

class Solution {
    fun minEliminationTime(timeReq: IntArray, splitTime: Int): Long {
        var pq = PriorityQueue<Int>()
        for (v in timeReq) { pq.offer(v) }
        while (pq.size > 1) {
            pq.poll()
            var x = pq.poll()
            pq.offer(x + splitTime)
        }
        return pq.peek()
    }
}
