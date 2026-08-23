// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

using System.Text;

public class Solution {
    public bool BackspaceCompare(string s, string t) {
        string Build(string text) {
            var stack = new StringBuilder();
            foreach (char ch in text) {
                if (ch == '#') {
                    if (stack.Length > 0) stack.Length--;
                } else stack.Append(ch);
            }
            return stack.ToString();
        }
        return Build(s) == Build(t);
    }
}
