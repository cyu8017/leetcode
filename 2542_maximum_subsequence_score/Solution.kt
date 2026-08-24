// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

class Solution {
    fun maxScore(nums1: IntArray, nums2: IntArray, k: Int): Long {
        val n = nums1.size
        val idx = Array(n) { it }
        idx.sortByDescending { nums2[it] }
        val pq = java.util.PriorityQueue<Int>()
        var sum = 0L
        var ans = 0L
        for (i in idx) {
            pq.offer(nums1[i])
            sum += nums1[i]
            if (pq.size > k) sum -= pq.poll()
            if (pq.size == k) {
                val cand = sum * nums2[i]
                if (cand > ans) ans = cand
            }
        }
        return ans
    }
}
