// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MakeGood(string s) {
        var stack = new List<char>();
        foreach (char ch in s) {
            if (stack.Count > 0 && stack[stack.Count - 1] != ch &&
                char.ToLower(stack[stack.Count - 1]) == char.ToLower(ch)) {
                stack.RemoveAt(stack.Count - 1);
            } else {
                stack.Add(ch);
            }
        }
        return new string(stack.ToArray());
    }
}
