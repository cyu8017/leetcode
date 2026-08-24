// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution {
    fun numberOfSubstrings(s: String): Int {
        var n = s.length
        var nxt = IntArray(n + 1)
        nxt[n] = n
        for (i in n - 1 downTo 0) {
            nxt[i] = nxt[i + 1]
            if (s[i] == '0') nxt[i] = i
        }
        var ans = 0
        for (i in 0 until n) {
            var cnt0 = if ((s[i] == '0')) 1 else 0
            var j = i
            while (j < n && cnt0 * cnt0 <= n) {
                var cnt1 = nxt[j + 1] - i - cnt0
                if (cnt1 >= cnt0 * cnt0) {
                    ans += minOf(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1)
                }
                j = nxt[j + 1]
                cnt0++
            }
        }
        return ans
    }
}
