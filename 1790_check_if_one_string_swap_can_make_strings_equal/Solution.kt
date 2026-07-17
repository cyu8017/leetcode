// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution {
    fun areAlmostEqual(s1: String, s2: String): Boolean {
        val diff = s1.indices.filter { s1[it] != s2[it] }
        if (diff.isEmpty()) return true
        return diff.size == 2 && s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]]
    }
}
