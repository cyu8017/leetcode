// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

class Solution {
    fun checkGoodInteger(n: Int): Boolean {
        var s = 0
        var x = n
        while (x > 0) {
            val d = x % 10
            s += d * (d - 1)
            x /= 10
        }
        return s >= 50
    }
}
