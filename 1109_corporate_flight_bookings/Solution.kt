// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

class Solution {
    fun corpFlightBookings(bookings: Array<IntArray>, n: Int): IntArray {
        val diff = IntArray(n + 1)
        for (b in bookings) {
            diff[b[0] - 1] += b[2]
            diff[b[1]] -= b[2]
        }
        val ans = IntArray(n)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            ans[i] = cur
        }
        return ans
    }
}
