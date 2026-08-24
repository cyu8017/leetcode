// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

class Solution {
    private fun isVowel(c: Char): Boolean {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }

    fun beautifulSubstrings(s: String, k: Int): Int {
        var ans = 0
        var n = s.length
        for (i in 0 until n) {
            var v = 0
            var c = 0
            for (j in i until n) {
                if (isVowel(s[j])) v++
                else c++
                if (v == c && (v * c) % k == 0) ans++
            }
        }
        return ans
    }
}
