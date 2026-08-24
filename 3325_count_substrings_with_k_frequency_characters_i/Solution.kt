// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

class Solution {
    fun numberOfSubstrings(s: String, k: Int): Int {
        val n = s.length
        var ans = 0
        for (i in 0 until n) {
            val freq = IntArray(26)
            for (j in i until n) {
                freq[s[j] - 'a']++
                var ok = false
                for (f in freq) {
                    if (f >= k) {
                        ok = true
                        break
                    }
                }
                if (ok) {
                    ans += n - j
                    break
                }
            }
        }
        return ans
    }
}
