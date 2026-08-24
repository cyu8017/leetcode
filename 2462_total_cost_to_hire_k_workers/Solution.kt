// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

import java.util.PriorityQueue

class Solution {
    fun totalCost(costs: IntArray, k: Int, candidates: Int): Long {
        val cmp = compareBy<IntArray>({ it[0] }, { it[1] })
        val leftH = PriorityQueue(cmp)
        val rightH = PriorityQueue(cmp)
        val n = costs.size
        var l = 0
        var r = n - 1
        while (l <= r && leftH.size < candidates) {
            leftH.offer(intArrayOf(costs[l], l))
            l++
        }
        while (r >= l && rightH.size < candidates) {
            rightH.offer(intArrayOf(costs[r], r))
            r--
        }
        var ans = 0L
        repeat(k) {
            var useLeft = false
            if (leftH.isNotEmpty() && rightH.isNotEmpty()) {
                val lt = leftH.peek()
                val rt = rightH.peek()
                if (lt[0] < rt[0] || (lt[0] == rt[0] && lt[1] <= rt[1])) useLeft = true
            } else if (leftH.isNotEmpty()) {
                useLeft = true
            }
            if (useLeft) {
                ans += leftH.poll()[0]
                if (l <= r) {
                    leftH.offer(intArrayOf(costs[l], l))
                    l++
                }
            } else {
                ans += rightH.poll()[0]
                if (l <= r) {
                    rightH.offer(intArrayOf(costs[r], r))
                    r--
                }
            }
        }
        return ans
    }
}
