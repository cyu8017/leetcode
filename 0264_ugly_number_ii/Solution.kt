// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

class Solution {
    fun nthUglyNumber(n: Int): Int {
        val ugly = mutableListOf(1)
        var index2 = 0
        var index3 = 0
        var index5 = 0
        while (ugly.size < n) {
            val nextUgly = minOf(
                ugly[index2] * 2,
                ugly[index3] * 3,
                ugly[index5] * 5,
            )
            ugly.add(nextUgly)
            if (nextUgly == ugly[index2] * 2) {
                index2++
            }
            if (nextUgly == ugly[index3] * 3) {
                index3++
            }
            if (nextUgly == ugly[index5] * 5) {
                index5++
            }
        }
        return ugly.last()
    }
}
