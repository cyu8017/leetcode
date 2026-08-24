// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

class Solution {
    fun internalAngles(sides: IntArray): DoubleArray {
        sides.sort()
        var a = sides[0]
        var b = sides[1]
        var c = sides[2]
        if (a + b <= c) return DoubleArray(0)
        var PI = Math.acos(-1.0)
        var A = Math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI
        var B = Math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI
        var C = 180.0 - A - B
        return double[] { A, B, C }
    }
}
