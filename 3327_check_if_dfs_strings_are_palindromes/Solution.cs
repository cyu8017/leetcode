// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

using System.Collections.Generic;
using System.Text;

public class Solution {
    bool IsPal(string s) {
        for (int i = 0, j = s.Length - 1; i < j; i++, j--) {
            if (s[i] != s[j]) return false;
        }
        return true;
    }

    public bool[] FindAnswer(int[] parent, string s) {
        int n = parent.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[parent[i]].Add(i);
        bool[] ans = new bool[n];
        string DfsStr(int u) {
            var sb = new StringBuilder();
            foreach (int v in g[u]) sb.Append(DfsStr(v));
            sb.Append(s[u]);
            string outStr = sb.ToString();
            ans[u] = IsPal(outStr);
            return outStr;
        }
        DfsStr(0);
        return ans;
    }
}
