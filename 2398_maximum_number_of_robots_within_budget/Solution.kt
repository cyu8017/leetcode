// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

import java.util.ArrayDeque

class Solution {
    fun maximumRobots(chargeTimes: IntArray, runningCosts: IntArray, budget: Long): Int {
        val n = chargeTimes.size
        var left = 0
        var sum = 0L
        val dq = ArrayDeque<Int>()
        var ans = 0
        for (right in 0 until n) {
            while (dq.isNotEmpty() && chargeTimes[dq.peekLast()] <= chargeTimes[right]) dq.pollLast()
            dq.addLast(right)
            sum += runningCosts[right]
            while (left <= right && chargeTimes[dq.peekFirst()].toLong() + (right - left + 1).toLong() * sum > budget) {
                if (dq.peekFirst() == left) dq.pollFirst()
                sum -= runningCosts[left]
                left++
            }
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
