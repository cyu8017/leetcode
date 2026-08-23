// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

using System.Collections.Generic;

public class Solution {
    public IList<int> RemainingMethods(int n, int k, int[][] invocations) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in invocations) g[e[0]].Add(e[1]);
        bool[] sus = new bool[n];
        void Dfs(int u) {
            if (sus[u]) return;
            sus[u] = true;
            foreach (int v in g[u]) Dfs(v);
        }
        Dfs(k);
        foreach (var e in invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                var all = new List<int>(n);
                for (int i = 0; i < n; i++) all.Add(i);
                return all;
            }
        }
        var ans = new List<int>();
        for (int i = 0; i < n; i++) if (!sus[i]) ans.Add(i);
        return ans;
    }
}
