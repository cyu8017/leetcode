// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution {
    fun findPermutationDifference(s: String, t: String): Int {
        var d = IntArray(26)
        for (i in 0 until s.length) { d[s[i] - 'a'] = i }
        var ans = 0
        for (i in 0 until t.length) { ans += kotlin.math.abs(d[t[i] - 'a'] - i) }
        return ans
    }
}
