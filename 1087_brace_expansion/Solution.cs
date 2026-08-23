// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] Expand(string s) {
        var groups = new List<List<string>>();
        int i = 0;
        while (i < s.Length) {
            if (s[i] == '{') {
                int j = s.IndexOf('}', i);
                var options = s.Substring(i + 1, j - i - 1).Split(',').OrderBy(x => x).ToList();
                groups.Add(options);
                i = j + 1;
            } else {
                groups.Add(new List<string> { s[i].ToString() });
                i++;
            }
        }
        var ans = new List<string> { "" };
        foreach (var group in groups) {
            var next = new List<string>();
            foreach (string prefix in ans) {
                foreach (string ch in group) {
                    next.Add(prefix + ch);
                }
            }
            ans = next;
        }
        return ans.ToArray();
    }
}
