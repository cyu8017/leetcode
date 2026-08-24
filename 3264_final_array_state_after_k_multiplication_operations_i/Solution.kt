// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

import java.util.PriorityQueue

class Solution {
    fun getFinalState(nums: IntArray, k: Int, multiplier: Int): IntArray {
        val h = PriorityQueue<IntArray> { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0]) else a[1].compareTo(b[1])
        }
        for (i in nums.indices) h.offer(intArrayOf(nums[i], i))
        repeat(k) {
            val cur = h.poll()
            val v = cur[0] * multiplier
            val i = cur[1]
            nums[i] = v
            h.offer(intArrayOf(v, i))
        }
        return nums
    }
}
