// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

class Solution {
    fun primePalindrome(n: Int): Int {
        if (n <= 2) return 2
        if (n <= 3) return 3
        if (n <= 5) return 5
        if (n <= 7) return 7
        if (n <= 11) return 11
        for (length in 1 until = 5) {
            var start = Math.pow(10, length - 1)
            var end = Math.pow(10, length)
            for (root in start until end) {
                var s = Integer.toString(root)
                var pal = StringBuilder(s)
                run {
                    var i = s.length - 2
                    while (i >= 0) {
                        pal.append(s[i])
                        i--
                    }
                }
                var `val` = pal.toString(.toInt())
                if (val >= n && isPrime(val)) return val
            }
        }
        return 0
    }

    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        if (x % 2 == 0) return x == 2
        run {
            var d = 3
            while (d * d <= x) {
                if (x % d == 0) return false
                d += 2
            }
        }
        return true
    }
}
