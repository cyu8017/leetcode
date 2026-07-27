// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

import java.util.PriorityQueue

class Solution {
    fun minimumDeviation(nums: IntArray): Int {
        val pq = PriorityQueue<Int>(compareByDescending { it })
        var mn = Int.MAX_VALUE
        for (v in nums) {
            var x = v
            if (x % 2 == 1) x *= 2
            mn = minOf(mn, x)
            pq.offer(x)
        }
        var ans = Int.MAX_VALUE
        while (true) {
            val x = pq.poll()
            ans = minOf(ans, x - mn)
            if (x % 2 == 1) return ans
            val half = x / 2
            mn = minOf(mn, half)
            pq.offer(half)
        }
    }
}
