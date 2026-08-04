// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution {
    public int minInsertions(String s) {
        int insertions = 0, needed = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                needed += 2;
                if ((needed & 1) == 1) {
                    insertions++;
                    needed--;
                }
            } else {
                needed--;
                if (needed < 0) {
                    insertions++;
                    needed = 1;
                }
            }
        }
        return insertions + needed;
    }
}
