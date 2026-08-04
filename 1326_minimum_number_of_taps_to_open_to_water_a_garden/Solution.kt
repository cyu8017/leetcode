// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution {
    fun minTaps(n: Int, ranges: IntArray): Int {
        val farthest = IntArray(n + 1)
        for (center in ranges.indices) {
            val radius = ranges[center]
            val left = maxOf(0, center - radius)
            val right = minOf(n, center + radius)
            farthest[left] = maxOf(farthest[left], right)
        }
        var taps = 0
        var end = 0
        var reach = 0
        for (position in 0 until n) {
            reach = maxOf(reach, farthest[position])
            if (position == end) {
                if (reach <= position) return -1
                taps++
                end = reach
            }
        }
        return taps
    }
}
