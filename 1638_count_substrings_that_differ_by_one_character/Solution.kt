// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution {
    fun countSubstrings(s: String, t: String): Int {
        var ans = 0
        for (i in s.indices) {
            for (j in t.indices) {
                var diff = 0
                var k = 0
                while (i + k < s.length && j + k < t.length) {
                    if (s[i + k] != t[j + k]) diff++
                    if (diff == 1) ans++
                    else if (diff > 1) break
                    k++
                }
            }
        }
        return ans
    }
}
