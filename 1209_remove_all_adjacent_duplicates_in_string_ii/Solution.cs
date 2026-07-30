// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string RemoveDuplicates(string s, int k) {
        var stack = new List<(char ch, int count)>();
        foreach (char ch in s) {
            if (stack.Count > 0 && stack[^1].ch == ch) {
                var top = stack[^1];
                stack[^1] = (top.ch, top.count + 1);
            } else {
                stack.Add((ch, 1));
            }
            if (stack[^1].count == k) stack.RemoveAt(stack.Count - 1);
        }
        var sb = new StringBuilder();
        foreach (var (ch, count) in stack) sb.Append(ch, count);
        return sb.ToString();
    }
}
