// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

class Solution {
    fun getCollisionTimes(cars: Array<IntArray>): DoubleArray {
        val n = cars.size
        val ans = DoubleArray(n) { -1.0 }
        val stack = ArrayDeque<Int>()
        for (i in n - 1 downTo 0) {
            val pos = cars[i][0]
            val speed = cars[i][1]
            while (stack.isNotEmpty()) {
                val j = stack.last()
                if (speed <= cars[j][1]) {
                    stack.removeLast()
                    continue
                }
                val t = (cars[j][0] - pos).toDouble() / (speed - cars[j][1])
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t
                    break
                }
                stack.removeLast()
            }
            stack.addLast(i)
        }
        return ans
    }
}
