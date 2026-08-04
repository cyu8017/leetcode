// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution {
    fun maxPerformance(n: Int, speed: IntArray, efficiency: IntArray, k: Int): Int {
        val engineers = efficiency.indices.map { i -> efficiency[i].toLong() to speed[i].toLong() }
            .sortedByDescending { it.first }
        val heap = java.util.PriorityQueue<Long>()
        var total = 0L
        var ans = 0L
        for ((e, s) in engineers) {
            heap.offer(s)
            total += s
            if (heap.size > k) total -= heap.poll()
            ans = maxOf(ans, total * e)
        }
        return (ans % 1_000_000_007L).toInt()
    }
}
