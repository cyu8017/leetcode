// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum_total_sum_with_threshold_constraints/

import java.util.PriorityQueue

class Solution {
    fun maxSum(nums: IntArray, threshold: IntArray): Long {
        val n = nums.size
        val idx = Array(n) { it }
        idx.sortBy { threshold[it] }
        val tree = PriorityQueue<Int>(compareByDescending { it })
        var ans = 0L
        var i = 0
        var step = 1
        while (true) {
            while (i < n && threshold[idx[i]] <= step) {
                tree.offer(nums[idx[i]])
                i++
            }
            if (tree.isEmpty()) break
            ans += tree.poll()
            step++
        }
        return ans
    }
}
