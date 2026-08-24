// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

class Solution {
    private fun isVowel(c: Char): Boolean {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }

    fun beautifulSubstrings(s: String, k: Int): Long {
        var x = 1
        while ((x * x) % k != 0) x++
        var freq = HashMap<Long, Int>()
        freq[0L] = 1
        var bal = 0
        var vowels = 0
        var ans = 0
        for (i in 0 until s.length) {
            var ch = s[i]
            if (isVowel(ch)) { bal++; vowels++; }
            else bal--
            var kk = ((bal) shl 32) | (vowels % x)
            var f = freq.getOrDefault(kk, 0)
            ans += f
            freq[kk] = f + 1
        }
        return ans
    }
}
