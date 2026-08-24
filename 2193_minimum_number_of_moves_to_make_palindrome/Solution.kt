// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution {
    fun minMovesToMakePalindrome(s: String): Int {
        StringBuilder b = StringBuilder(s)
        var ans: Int = 0
        while (b.length > 1) {
            var j: Int = b.length - 1
            while (j > 0 && b[j] != b[0]) j--
            if (j == 0) {
                ans += b.length / 2
                b.deleteCharAt(0)
                continue
            }
            ans += b.length - 1 - j
            b.deleteCharAt(j)
            b.deleteCharAt(0)
        }
        return ans
    }
}
