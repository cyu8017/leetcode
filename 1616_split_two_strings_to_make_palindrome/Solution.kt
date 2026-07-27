// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution {
    fun checkPalindromeFormation(a: String, b: String): Boolean {
        fun isPal(s: String, i: Int, j: Int): Boolean {
            var l = i
            var r = j
            while (l < r) {
                if (s[l] != s[r]) return false
                l++
                r--
            }
            return true
        }
        fun check(x: String, y: String): Boolean {
            var i = 0
            var j = x.length - 1
            while (i < j && x[i] == y[j]) {
                i++
                j--
            }
            return isPal(x, i, j) || isPal(y, i, j)
        }
        return check(a, b) || check(b, a)
    }
}
