// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

using System.Collections.Generic;

public class Solution {
    public double MaxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        var graph = new List<(int, double)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, double)>();
        for (int i = 0; i < edges.Length; i++) {
            int a = edges[i][0], b = edges[i][1];
            graph[a].Add((b, succProb[i]));
            graph[b].Add((a, succProb[i]));
        }
        var pq = new PriorityQueue<(double prob, int node), double>();
        double[] best = new double[n];
        best[start_node] = 1.0;
        pq.Enqueue((1.0, start_node), -1.0);
        while (pq.Count > 0) {
            var (probability, node) = pq.Dequeue();
            if (node == end_node) return probability;
            if (probability < best[node]) continue;
            foreach (var (neighbor, edgeProb) in graph[node]) {
                double candidate = probability * edgeProb;
                if (candidate > best[neighbor]) {
                    best[neighbor] = candidate;
                    pq.Enqueue((candidate, neighbor), -candidate);
                }
            }
        }
        return 0.0;
    }
}
