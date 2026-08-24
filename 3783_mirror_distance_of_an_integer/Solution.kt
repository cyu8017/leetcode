// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror_distance_of_an_integer/

class Solution {
    fun mirrorDistance(n: Int): Int {
        return kotlin.math.abs(n - reverse(n))
    }

    private fun reverse(x: Int): Int {
        var y = 0
        while (x > 0) {
y = y * 10 + x % 10
        return y
    }
}
x /= 10
}
