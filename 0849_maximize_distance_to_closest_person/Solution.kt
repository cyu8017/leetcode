// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution {
    fun maxDistToClosest(seats: IntArray): Int {
        var n = seats.size
        var prev = -1
        var ans = 0
        for (i in 0 until n) {
            if (seats[i] == 1) {
                if (prev == -1) ans = i
                else ans = maxOf(ans, (i - prev) / 2)
                prev = i
            }
        }
        return maxOf(ans, n - 1 - prev)
    }
}
