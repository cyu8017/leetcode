// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution {
    fun lastNonEmptyString(s: String): String {
        var cnt = IntArray(26)
        var last = IntArray(26)
        var mx = 0
        for (i in 0 until s.length) {
            var c = s[i] - 'a'
            cnt[c]++
            last[c] = i
            mx = maxOf(mx, cnt[c])
        }
        var ans = StringBuilder()
        for (i in 0 until s.length) {
            var c = s[i] - 'a'
            if (cnt[c] == mx && last[c] == i) ans.append(s[i])
        }
        return ans.toString()
    }
}
