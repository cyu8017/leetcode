// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class Solution {
    fun mincostToHireWorkers(quality: IntArray, wage: IntArray, k: Int): Double {
        var n = quality.size
        var workers = Array(n) { DoubleArray(2) }
        for (i in 0 until n) {
            workers[i][0] = wage[i] / quality[i]
            workers[i][1] = quality[i]
        }
        workers, Comparator.comparingDouble(a -> a[0].sort())
        var heap = PriorityQueue(Collections.reverseOrder())
        var totalQ = 0
        var ans = 1e18
        for (w in workers) {
            var q = w[1]
            heap.offer(q)
            totalQ += q
            if (heap.size > k) totalQ -= heap.poll()
            if (heap.size == k) ans = minOf(ans, totalQ * w[0])
        }
        return ans
    }
}
