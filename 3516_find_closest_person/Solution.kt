// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

class Solution {
    fun findClosest(x: Int, y: Int, z: Int): Int {
        var a = kotlin.math.abs(x - z)
        var b = kotlin.math.abs(y - z)
        if (a == b) return 0
        return if (a < b) 1 else 2
    }
}
