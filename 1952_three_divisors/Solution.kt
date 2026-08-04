// LeetCode 1952
// https://leetcode.com/problems/three-divisors/

class Solution {
    fun isThree(n: Int): Boolean {
        val root = kotlin.math.sqrt(n.toDouble()).toInt()
        if (root * root != n || root < 2) return false
        var i = 2
        while (i * i <= root) {
            if (root % i == 0) return false
            i++
        }
        return true
    }
}
