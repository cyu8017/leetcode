// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

class Solution {
    fun numberOfBoomerangs(points: Array<IntArray>): Int {
        var total = 0
        for (anchor in points) {
            val distances = HashMap<Long, Int>()
            for (other in points) {
                val dx = anchor[0] - other[0]
                val dy = anchor[1] - other[1]
                val distance = dx.toLong() * dx + dy.toLong() * dy
                distances[distance] = distances.getOrDefault(distance, 0) + 1
            }
            for (count in distances.values) {
                total += count * (count - 1)
            }
        }
        return total
    }
}
