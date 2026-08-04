// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution {
    fun maxDistance(position: IntArray, m: Int): Int {
        position.sort()
        var lo = 1
        var hi = (position[position.size - 1] - position[0]) / (m - 1)
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            var count = 1
            var last = position[0]
            for (i in 1 until position.size) {
                if (position[i] - last >= mid) {
                    count++
                    last = position[i]
                }
            }
            if (count >= m) lo = mid + 1 else hi = mid - 1
        }
        return hi
    }
}
