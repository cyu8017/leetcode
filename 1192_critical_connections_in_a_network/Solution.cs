// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> CriticalConnections(int n, IList<IList<int>> connections) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var c in connections) {
            graph[c[0]].Add(c[1]);
            graph[c[1]].Add(c[0]);
        }

        var disc = new int[n];
        var low = new int[n];
        Array.Fill(disc, -1);
        Array.Fill(low, -1);
        int time = 0;
        var bridges = new List<IList<int>>();

        void Dfs(int node, int parent) {
            disc[node] = low[node] = time++;
            foreach (int nxt in graph[node]) {
                if (nxt == parent) continue;
                if (disc[nxt] == -1) {
                    Dfs(nxt, node);
                    low[node] = Math.Min(low[node], low[nxt]);
                    if (low[nxt] > disc[node]) {
                        bridges.Add(new List<int> { Math.Min(node, nxt), Math.Max(node, nxt) });
                    }
                } else {
                    low[node] = Math.Min(low[node], disc[nxt]);
                }
            }
        }

        Dfs(0, -1);
        return bridges;
    }
}
