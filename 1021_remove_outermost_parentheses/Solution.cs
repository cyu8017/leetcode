// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

using System.Text;

public class Solution {
    public string RemoveOuterParentheses(string s) {
        var ans = new StringBuilder();
        int depth = 0;
        foreach (char ch in s) {
            if (ch == '(') {
                if (depth > 0) ans.Append(ch);
                depth++;
            } else {
                depth--;
                if (depth > 0) ans.Append(ch);
            }
        }
        return ans.ToString();
    }
}
