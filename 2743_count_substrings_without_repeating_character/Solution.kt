// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    fun numberOfSpecialSubstrings(s: String): Int {
        var n = s.length
        var ans = 0
        var left = 0
        var cnt = IntArray(26)
        for (i in 0 until n) {
            var c = s[i] - 'a'
            cnt[c]++
            while (cnt[c] > 1) { cnt[s[left] - 'a']--; left++; }
            ans += i - left + 1
        }
        return ans
    }
}
