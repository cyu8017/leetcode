// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

class Solution {
    fun mirrorReflection(p: Int, q: Int): Int {
        var p = p
        var q = q
        var g = gcd(p, q)
        p /= g
        q /= g
        if (p % 2 == 0) return 2
        if (q % 2 == 0) return 0
        return 1
    }

    private fun gcd(a: Int, b: Int): Int {
        var a = a
        var b = b
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }
}
