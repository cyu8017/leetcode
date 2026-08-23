// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

using System.Collections.Generic;

public class Solution {
    public bool IsValid(string code) {
        var stack = new List<string>();
        int i = 0, n = code.Length;
        while (i < n) {
            if (i + 9 <= n && code.Substring(i, 9) == "<![CDATA[") {
                if (stack.Count == 0) return false;
                int j = code.IndexOf("]]>", i + 9);
                if (j < 0) return false;
                i = j + 3;
            } else if (i + 2 <= n && code.Substring(i, 2) == "</") {
                int j = code.IndexOf('>', i + 2);
                if (j < 0) return false;
                string tag = code.Substring(i + 2, j - i - 2);
                if (stack.Count == 0 || stack[^1] != tag) return false;
                stack.RemoveAt(stack.Count - 1);
                i = j + 1;
                if (stack.Count == 0 && i < n) return false;
            } else if (code[i] == '<') {
                int j = code.IndexOf('>', i + 1);
                if (j < 0) return false;
                string tag = code.Substring(i + 1, j - i - 1);
                if (tag.Length == 0 || tag.Length > 9) return false;
                foreach (char ch in tag) {
                    if (ch < 'A' || ch > 'Z') return false;
                }
                stack.Add(tag);
                i = j + 1;
            } else {
                if (stack.Count == 0) return false;
                ++i;
            }
        }
        return stack.Count == 0;
    }
}
