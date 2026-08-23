// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

using System.Collections.Generic;

public class Solution {
    public int[] FindSubtreeSizes(int[] parent, string s) {
        int n = parent.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[parent[i]].Add(i);
        int[] newParent = (int[])parent.Clone();
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) last[i] = -1;
        void Dfs1(int u) {
            int c = s[u] - 'a';
            int prev = last[c];
            if (prev != -1) newParent[u] = prev;
            last[c] = u;
            foreach (int v in g[u]) Dfs1(v);
            last[c] = prev;
        }
        Dfs1(0);
        var ng = new List<int>[n];
        for (int i = 0; i < n; i++) ng[i] = new List<int>();
        for (int i = 1; i < n; i++) ng[newParent[i]].Add(i);
        int[] ans = new int[n];
        int Dfs2(int u) {
            int sz = 1;
            foreach (int v in ng[u]) sz += Dfs2(v);
            return ans[u] = sz;
        }
        Dfs2(0);
        return ans;
    }
}
