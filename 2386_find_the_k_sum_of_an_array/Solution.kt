// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

import java.util.PriorityQueue

class Solution {
    fun kSum(nums: IntArray, k: Int): Long {
        var total = 0L
        val n = nums.size
        val absNums = IntArray(n)
        for (i in 0 until n) {
            if (nums[i] >= 0) {
                total += nums[i]
                absNums[i] = nums[i]
            } else {
                absNums[i] = -nums[i]
            }
        }
        absNums.sort()
        val h = PriorityQueue<LongArray>(compareByDescending { it[0] })
        h.offer(longArrayOf(total, 0))
        repeat(k - 1) {
            val cur = h.poll()
            val sum = cur[0]
            val i = cur[1].toInt()
            if (i >= absNums.size) return@repeat
            h.offer(longArrayOf(sum - absNums[i], (i + 1).toLong()))
            if (i > 0) {
                h.offer(longArrayOf(sum - absNums[i] + absNums[i - 1], (i + 1).toLong()))
            }
        }
        return h.peek()[0]
    }
}
