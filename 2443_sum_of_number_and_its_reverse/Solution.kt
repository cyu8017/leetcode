// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution {
    fun sumOfNumberAndReverse(num: Int): Boolean {
        for (i in 0..num) {
            if (i + rev(i) == num) return true
        }
        return false
    }

    private fun rev(x0: Int): Int {
        var x = x0
        var r = 0
        while (x > 0) {
            r = r * 10 + x % 10
            x /= 10
        }
        return r
    }
}
