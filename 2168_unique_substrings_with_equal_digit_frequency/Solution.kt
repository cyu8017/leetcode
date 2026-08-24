// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

class Solution {
    fun equalDigitFrequency(s: String): Int {
        var n: Int = s.length
        var seen = HashSet()
        for (i in 0 until n) {
            var freq: IntArray = IntArray(10)
            var maxf: Int = 0, kinds = 0
            for (j in i until n) {
                var d: Int = s[j] - '0'
                if (freq[d] == 0) kinds++
                freq[d]++
                maxf = maxOf(maxf, freq[d])
                if (maxf * kinds == j - i + 1) seen.add(s.substring(i, j + 1))
            }
        }
        return seen.size
    }
}
