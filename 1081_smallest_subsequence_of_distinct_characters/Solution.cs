// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string SmallestSubsequence(string s) {
        var last = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++) {
            last[s[i]] = i;
        }
        var stack = new List<char>();
        var used = new HashSet<char>();
        for (int i = 0; i < s.Length; i++) {
            char ch = s[i];
            if (used.Contains(ch)) {
                continue;
            }
            while (stack.Count > 0 && ch < stack[stack.Count - 1] && last[stack[stack.Count - 1]] > i) {
                used.Remove(stack[stack.Count - 1]);
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(ch);
            used.Add(ch);
        }
        return new string(stack.ToArray());
    }
}
