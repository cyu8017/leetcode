// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

class Solution {
    fun isReachable(targetX: Int, targetY: Int): Boolean {
        var g = Gcd(targetX, targetY)
        while (g % 2 == 0) g /= 2
        return g == 1
    }

    fun Gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }
}
