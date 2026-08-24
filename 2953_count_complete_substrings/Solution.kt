// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

class Solution {
    fun countCompleteSubstrings(word: String, k: Int): Int {
        val n = word.length
        var ans = 0
        var i = 0
        while (i < n) {
            var j = i
            while (j + 1 < n && kotlin.math.abs(word[j + 1] - word[j]) <= 2) j++
            val seg = word.substring(i, j + 1)
            val m = seg.length
            for (chars in 1..26) {
                val length = chars * k
                if (length > m) break
                val freq = IntArray(26)
                var unique = 0
                for (r in 0 until m) {
                    val c = seg[r] - 'a'
                    freq[c]++
                    if (freq[c] == 1) unique++
                    if (r >= length) {
                        val c2 = seg[r - length] - 'a'
                        freq[c2]--
                        if (freq[c2] == 0) unique--
                    }
                    if (r >= length - 1 && unique == chars) {
                        var ok = true
                        for (f in freq) if (f != 0 && f != k) { ok = false; break }
                        if (ok) ans++
                    }
                }
            }
            i = j + 1
        }
        return ans
    }
}
