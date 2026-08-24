// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution {
    fun countBalls(lowLimit: Int, highLimit: Int): Int {
        val counts = HashMap<Int, Int>()
        for (value in lowLimit..highLimit) {
            var box = 0
            var v = value
            while (v > 0) {
                box += v % 10
                v /= 10
            }
            counts[box] = (counts[box] ?: 0) + 1
        }
        return counts.values.max()
    }
}
