// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution {
    fun repeatLimitedString(s: String, repeatLimit: Int): String {
        var freq: IntArray = IntArray(26)
        for (i in 0 until s.length) freq[s[i] - 'a']++
        StringBuilder ans = StringBuilder()
        while (true) {
            var placed: Boolean = false
            for (c in 25 downTo 0) {
                if (freq[c] == 0) continue
                if (ans.length > 0 && ans[ans.size(] - 1) - 'a' == c) {
                    var found: Boolean = false
                    for (d in c - 1 downTo 0) {
                        if (freq[d] > 0) {
                            ans.append(('a' + d))
                            freq[d]--
                            found = placed = true
                            break
                        }
                    }
                    if (!found) return ans.toString()
                    break
                }
                var use: Int = minOf(freq[c], repeatLimit)
                for (i in 0 until use) ans.append(('a' + c))
                freq[c] -= use
                placed = true
                break
            }
            if (!placed) break
        }
        return ans.toString()
    }
}
