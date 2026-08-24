// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution {
    fun maxHeightOfTriangle(red: Int, blue: Int): Int {
        var ans = 0
        for (k in 0 until 2) {
            val c = intArrayOf(red, blue)
            var i = 1
            var j = k
            while (i <= c[j]) {
                c[j] -= i
                ans = maxOf(ans, i)
                i++
                j = j xor 1
            }
        }
        return ans
    }
}
