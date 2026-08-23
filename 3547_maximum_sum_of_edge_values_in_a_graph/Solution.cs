// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

using System;
using System.Collections.Generic;

public class Solution {
    long Calc(int left, int right, bool isCycle) {
        int w0 = right, w1 = right;
        long score = 0;
        for (int value = right - 1; value >= left; value--) {
            score += 1L * w0 * value;
            w0 = w1;
            w1 = value;
        }
        if (isCycle) score += 1L * w0 * w1;
        return score;
    }
    public long MaxScore(int n, int[][] edges) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        bool[] seen = new bool[n];
        var cycleSizes = new List<int>();
        var pathSizes = new List<int>();
        List<int> GetComp(int start) {
            var comp = new List<int> { start };
            seen[start] = true;
            for (int i = 0; i < comp.Count; i++) {
                foreach (int v in graph[comp[i]]) {
                    if (!seen[v]) { seen[v] = true; comp.Add(v); }
                }
            }
            return comp;
        }
        for (int i = 0; i < n; i++) {
            if (seen[i]) continue;
            var comp = GetComp(i);
            bool allDeg2 = true;
            foreach (int u in comp) if (graph[u].Count != 2) { allDeg2 = false; break; }
            if (allDeg2) cycleSizes.Add(comp.Count);
            else if (comp.Count > 1) pathSizes.Add(comp.Count);
        }
        long ans = 0;
        int curN = n;
        foreach (int cs in cycleSizes) {
            ans += Calc(curN - cs + 1, curN, true);
            curN -= cs;
        }
        pathSizes.Sort((a, b) => b.CompareTo(a));
        foreach (int ps in pathSizes) {
            ans += Calc(curN - ps + 1, curN, false);
            curN -= ps;
        }
        return ans;
    }
}
