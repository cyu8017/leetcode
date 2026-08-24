// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

class Solution {
    fun diStringMatch(s: String): IntArray {
        var lo = 0
        var hi = s.length
        val ans = IntArray(s.length + 1)
        var k = 0
        for (ch in s) {
            if (ch == 'I') ans[k++] = lo++
            else ans[k++] = hi--
        }
        ans[k] = lo
        return ans
    }
}
