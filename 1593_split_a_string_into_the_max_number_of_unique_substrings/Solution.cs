// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxUniqueSplit(string s) {
        var used = new HashSet<string>();
        int answer = 0;

        void Dfs(int i) {
            if (used.Count + s.Length - i <= answer) return;
            if (i == s.Length) {
                answer = Math.Max(answer, used.Count);
                return;
            }
            for (int j = i + 1; j <= s.Length; j++) {
                string part = s.Substring(i, j - i);
                if (used.Add(part)) {
                    Dfs(j);
                    used.Remove(part);
                }
            }
        }
        Dfs(0);
        return answer;
    }
}
