// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution {
    fun minimumLength(s: String): Int {
        var cnt = IntArray(26)
        for (i in 0 until s.length) { cnt[s[i] - 'a']++ }
        var ans = 0
        for (x in cnt) {
            if (x > 0) ans += (x & 1) !=if (0) 1 else 2
        }
        return ans
    }
}
