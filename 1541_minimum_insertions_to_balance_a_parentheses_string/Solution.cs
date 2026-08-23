// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

public class Solution {
    public int MinInsertions(string s) {
        int insertions = 0, needed = 0;
        foreach (char ch in s) {
            if (ch == '(') {
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
