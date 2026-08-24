// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.isEmpty()) {
            return ""
        }

        for (i in strs[0].indices) {
            val ch = strs[0][i]
            for (j in 1 until strs.size) {
                if (i >= strs[j].length || strs[j][i] != ch) {
                    return strs[0].substring(0, i)
                }
            }
        }

        return strs[0]
    }
}
