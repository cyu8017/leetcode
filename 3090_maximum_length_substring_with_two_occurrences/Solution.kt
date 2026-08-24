// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution {
    fun maximumLengthSubstring(s: String): Int {
        var l = 0
        var ans = 0
        var cnt = IntArray(26)
        for (r in 0 until s.length) {
            var idx = s[r] - 'a'
            cnt[idx]++
            while (cnt[idx] > 2) {
                cnt[s[l] - 'a']--
                l++
            }
            ans = maxOf(ans, r - l + 1)
        }
        return ans
    }
}
