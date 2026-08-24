// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

class Solution {
    fun maxPoints(points: Array<IntArray>): Int {
        var best = 0
        for (i in points.indices) {
            val slopes = HashMap<Pair<Int, Int>, Int>(); var local = 1
            for (j in i + 1 until points.size) {
                var dx = points[j][0] - points[i][0]; var dy = points[j][1] - points[i][1]
                val divisor = gcd(dx, dy); dx /= divisor; dy /= divisor
                if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy }
                val key = Pair(dx, dy); slopes[key] = (slopes[key] ?: 0) + 1
                local = maxOf(local, slopes[key]!! + 1)
            }
            best = maxOf(best, local)
        }
        return best
    }
    private fun gcd(first: Int, second: Int): Int {
        var a = kotlin.math.abs(first); var b = kotlin.math.abs(second)
        while (b != 0) { val temp = a % b; a = b; b = temp }
        return a
    }
}