// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

class Solution {
    fun asteroidsDestroyed(mass: Int, asteroids: IntArray): Boolean {
        asteroids.sort()
        var cur: Long = mass
        for (a in asteroids) {
            if (cur < a) return false
            cur += a
        }
        return true
    }
}
