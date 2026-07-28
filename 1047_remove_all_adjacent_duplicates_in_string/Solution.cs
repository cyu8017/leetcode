// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

using System.Text;

public class Solution {
    public string RemoveDuplicates(string s) {
        var stack = new StringBuilder();
        foreach (char ch in s) {
            if (stack.Length > 0 && stack[^1] == ch) stack.Length--;
            else stack.Append(ch);
        }
        return stack.ToString();
    }
}
