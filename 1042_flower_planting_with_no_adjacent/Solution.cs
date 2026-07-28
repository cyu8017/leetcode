// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

using System.Collections.Generic;

public class Solution {
    public int[] GardenNoAdj(int n, int[][] paths) {
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        foreach (var p in paths) {
            graph[p[0]].Add(p[1]);
            graph[p[1]].Add(p[0]);
        }
        var ans = new int[n + 1];
        for (int garden = 1; garden <= n; garden++) {
            var used = new HashSet<int>();
            foreach (int nei in graph[garden]) used.Add(ans[nei]);
            for (int c = 1; c <= 4; c++) {
                if (!used.Contains(c)) { ans[garden] = c; break; }
            }
        }
        var result = new int[n];
        Array.Copy(ans, 1, result, 0, n);
        return result;
    }
}
