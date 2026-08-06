// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

class Solution {
    fun findMaxValueOfEquation(points: Array<IntArray>, k: Int): Int {
        val q = ArrayDeque<IntArray>()
        var ans = Int.MIN_VALUE / 2
        for (point in points) {
            val x = point[0]
            val y = point[1]
            while (q.isNotEmpty() && x - q.first()[0] > k) q.removeFirst()
            if (q.isNotEmpty()) ans = maxOf(ans, x + y + q.first()[1])
            val value = y - x
            while (q.isNotEmpty() && q.last()[1] <= value) q.removeLast()
            q.add(intArrayOf(x, value))
        }
        return ans
    }
}
