// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

class Solution {
    fun climbStairs(n: Int): Int {
        if (n <= 2) {
            return n
        }

        var prev = 1
        var curr = 2

        for (i in 3..n) {
            val next = prev + curr
            prev = curr
            curr = next
        }

        return curr
    }
}
