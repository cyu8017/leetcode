// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

using System.Collections.Generic;

public class Solution {
    public long CountPalindromePaths(IList<int> parent, string s) {
        int n = parent.Count;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[parent[i]].Add(i);
        var freq = new Dictionary<int, int>();
        freq[0] = 1;
        long ans = 0;
        void Dfs(int u, int mask) {
            foreach (int v in g[u]) {
                int nm = mask ^ (1 << (s[v] - 'a'));
                if (freq.TryGetValue(nm, out int c0)) ans += c0;
                for (int b = 0; b < 26; b++) {
                    int key = nm ^ (1 << b);
                    if (freq.TryGetValue(key, out int c)) ans += c;
                }
                if (!freq.ContainsKey(nm)) freq[nm] = 0;
                freq[nm]++;
                Dfs(v, nm);
            }
        }
        Dfs(0, 0);
        return ans;
    }
}
