// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

class Solution {
    fun closestFair(n: Int): Int {
        var x = n
        while (true) {
            val s = x.toString()
            if (s.length % 2 != 0) {
                var p = 1
                repeat(s.length) { p *= 10 }
                return closestFair(p)
            }
            var even = 0
            var odd = 0
            for (c in s) {
                if ((c - '0') % 2 == 0) even++ else odd++
            }
            if (even == odd) return x
            x++
        }
    }
}
