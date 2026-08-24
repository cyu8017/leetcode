// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution {
    fun minInsertions(s: String): Int {
        var insertions = 0
        var needed = 0
        for (ch in s) {
            if (ch == '(') {
                needed += 2
                if ((needed and 1) == 1) {
                    insertions++
                    needed--
                }
            } else {
                needed--
                if (needed < 0) {
                    insertions++
                    needed = 1
                }
            }
        }
        return insertions + needed
    }
}
