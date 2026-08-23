// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

using System.Collections.Generic;

public class Solution {
    public int[] LoudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in richer) graph[e[1]].Add(e[0]);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        int Dfs(int person) {
            if (ans[person] != -1) return ans[person];
            int best = person;
            foreach (int richerPerson in graph[person]) {
                int cand = Dfs(richerPerson);
                if (quiet[cand] < quiet[best]) best = cand;
            }
            return ans[person] = best;
        }
        for (int i = 0; i < n; i++) Dfs(i);
        return ans;
    }
}
