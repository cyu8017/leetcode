// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution {
    fun maxActiveSectionsAfterTrade(s: String, queries: Array<IntArray>): IntArray {
        var ones = 0
        for (c in s.toCharArray()) { if (c == '1') ones++ }
        var ans = IntArray(queries.size)
        for (i in 0 until ans.size) { ans[i] = ones }
        return ans
    }
}
