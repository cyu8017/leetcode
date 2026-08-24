// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

class Solution {
    fun findRadius(houses: IntArray, heaters: IntArray): Int {
        val sortedHeaters = heaters.sorted().toIntArray()
        var radius = 0
        for (house in houses) {
            var position = sortedHeaters.binarySearch(house)
            if (position < 0) {
                position = -position - 1
            }
            var best = Int.MAX_VALUE
            if (position < sortedHeaters.size) {
                best = minOf(best, kotlin.math.abs(sortedHeaters[position] - house))
            }
            if (position > 0) {
                best = minOf(best, kotlin.math.abs(sortedHeaters[position - 1] - house))
            }
            radius = maxOf(radius, best)
        }
        return radius
    }
}
