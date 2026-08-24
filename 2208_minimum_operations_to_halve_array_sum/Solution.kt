// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

import java.util.PriorityQueue

class Solution {
    fun halveArray(nums: IntArray): Int {
        val h = PriorityQueue<Double> { a, b -> java.lang.Double.compare(b, a) }
        var sum = 0.0
        for (x in nums) {
            h.offer(x.toDouble())
            sum += x
        }
        val target = sum / 2
        var ans = 0
        while (sum > target) {
            val top = h.poll()
            val x = top / 2
            sum -= x
            h.offer(x)
            ans++
        }
        return ans
    }
}
