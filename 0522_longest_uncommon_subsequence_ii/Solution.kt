// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution {
    fun findLUSlength(strs: Array<String>): Int {
        var result = -1
        for (i in strs.indices) {
            if (strs.indices.any { j -> i != j && isSubsequence(strs[i], strs[j]) }) {
                continue
            }
            result = maxOf(result, strs[i].length)
        }
        return result
    }

    private fun isSubsequence(target: String, source: String): Boolean {
        var index = 0
        for (char in source) {
            if (index < target.length && target[index] == char) {
                index++
            }
        }
        return index == target.length
    }
}
