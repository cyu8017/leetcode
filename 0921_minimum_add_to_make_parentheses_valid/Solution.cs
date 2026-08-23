// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

public class Solution {
    public int MinAddToMakeValid(string s) {
        int openNeed = 0, closeNeed = 0;
        foreach (char ch in s) {
            if (ch == '(') closeNeed++;
            else if (closeNeed > 0) closeNeed--;
            else openNeed++;
        }
        return openNeed + closeNeed;
    }
}
