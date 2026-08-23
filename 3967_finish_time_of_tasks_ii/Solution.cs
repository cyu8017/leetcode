// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

using System;
using System.Collections.Generic;

public class Solution {
    private struct Edge {
        public int To, Reverse;
        public Edge(int to, int reverse) { To = to; Reverse = reverse; }
    }

    static long Combine(long minimum, long maximum, int count, int bas) {
        if (count == 0) return bas;
        return 2 * maximum - minimum + bas;
    }

    public long MinFinishTime(int n, int[][] edges, int[] baseTime) {
        var graph = new List<Edge>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<Edge>();
        foreach (var edge in edges) {
            int u = edge[0], v = edge[1];
            int iu = graph[u].Count, iv = graph[v].Count;
            graph[u].Add(new Edge(v, iv));
            graph[v].Add(new Edge(u, iu));
        }
        int[] parent = new int[n], parentEdge = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -2;
        parent[0] = -1;
        var order = new List<int> { 0 };
        for (int i = 0; i < order.Count; i++) {
            int u = order[i];
            foreach (var edge in graph[u]) {
                if (parent[edge.To] == -2) {
                    parent[edge.To] = u;
                    parentEdge[edge.To] = edge.Reverse;
                    order.Add(edge.To);
                }
            }
        }
        var incoming = new long[n][];
        for (int i = 0; i < n; i++) incoming[i] = new long[graph[i].Count];
        for (int oi = n - 1; oi > 0; oi--) {
            int u = order[oi];
            long minimum = 1L << 62, maximum = -1;
            int count = 0;
            for (int edgeIndex = 0; edgeIndex < incoming[u].Length; edgeIndex++) {
                if (edgeIndex == parentEdge[u]) continue;
                long value = incoming[u][edgeIndex];
                minimum = Math.Min(minimum, value);
                maximum = Math.Max(maximum, value);
                count++;
            }
            long value2 = Combine(minimum, maximum, count, baseTime[u]);
            int parentNode = parent[u];
            int reverseIndex = graph[u][parentEdge[u]].Reverse;
            incoming[parentNode][reverseIndex] = value2;
        }
        long answer = 1L << 62;
        foreach (int u in order) {
            long min1 = 1L << 62, min2 = 1L << 62;
            int minIndex = -1;
            long max1 = -1, max2 = -1;
            int maxIndex = -1;
            for (int i = 0; i < incoming[u].Length; i++) {
                long value = incoming[u][i];
                if (value < min1) { min2 = min1; min1 = value; minIndex = i; }
                else if (value < min2) min2 = value;
                if (value > max1) { max2 = max1; max1 = value; maxIndex = i; }
                else if (value > max2) max2 = value;
            }
            long rootValue = Combine(min1, max1, graph[u].Count, baseTime[u]);
            answer = Math.Min(answer, rootValue);
            for (int i = 0; i < graph[u].Count; i++) {
                var edge = graph[u][i];
                if (edge.To == parent[u]) continue;
                if (graph[u].Count == 1) {
                    incoming[edge.To][edge.Reverse] = baseTime[u];
                    continue;
                }
                long minimum = min1, maximum = max1;
                if (i == minIndex) minimum = min2;
                if (i == maxIndex) maximum = max2;
                incoming[edge.To][edge.Reverse] = Combine(minimum, maximum, graph[u].Count - 1, baseTime[u]);
            }
        }
        return answer;
    }
}
