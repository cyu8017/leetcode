// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

class Solution {
    fun countSubstrings(s: String): Long {
        var ans = 0
        var n = s.length
        for (r in 0 until n) {
            var last = s[r] - '0'
            if (last == 0) continue
            var mod = 0
            var p = 1 % last
            for (l in r downTo 0) {
                mod = (mod + (s[l] - '0') * p) % last
                p = (p * 10) % last
                if (mod == 0) ans++
            }
        }
        return ans
    }
}
