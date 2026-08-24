// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution {
    fun smallestPalindrome(s: String): String {
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        var t = StringBuilder()
        var ch = 0
        var c: Char = 'a'
while (c <= 'z') {

            var v = cnt[c - 'a'] / 2
            for (i in 0 until v) { t.append(c) }
            cnt[c - 'a'] -= v * 2
            if (cnt[c - 'a'] == 1) ch = c
c = c + 1
}
        var sb = StringBuilder(t)
        if (ch != 0) sb.append(ch)
        run {
            var i = t.length - 1
            while (i >= 0) {
                sb.append(t[i])
                i = i - 1
            }
        }
        return sb.toString()
    }
}
