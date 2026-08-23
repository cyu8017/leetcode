// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ClearStars(string s) {
        var g = new List<int>[26];
        for (int i = 0; i < 26; i++) g[i] = new List<int>();
        int n = s.Length;
        bool[] rem = new bool[n];
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') {
                rem[i] = true;
                for (int j = 0; j < 26; j++) {
                    if (g[j].Count > 0) {
                        rem[g[j][g[j].Count - 1]] = true;
                        g[j].RemoveAt(g[j].Count - 1);
                        break;
                    }
                }
            } else {
                g[s[i] - 'a'].Add(i);
            }
        }
        var ans = new StringBuilder();
        for (int i = 0; i < n; i++) if (!rem[i]) ans.Append(s[i]);
        return ans.ToString();
    }
}
