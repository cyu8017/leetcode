// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

class Solution {
    fun numberOfSubstrings(s: String, k: Int): Long {
        val n = s.length
        var ans = 0L
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
                    ans += (n - j).toLong()
                    break
                }
            }
        }
        return ans
    }
}
