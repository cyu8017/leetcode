// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

import java.util.ArrayDeque

class Solution {
    fun constrainedSubsetSum(nums: IntArray, k: Int): Int {
        val queue = ArrayDeque<Int>()
        val best = nums.copyOf()
        for (i in nums.indices) {
            while (queue.isNotEmpty() && queue.first() < i - k) queue.removeFirst()
            best[i] = nums[i] + maxOf(0, if (queue.isEmpty()) 0 else best[queue.first()])
            while (queue.isNotEmpty() && best[queue.last()] <= best[i]) queue.removeLast()
            queue.addLast(i)
        }
        return best.maxOrNull() ?: 0
    }
}
