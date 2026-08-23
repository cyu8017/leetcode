// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSubtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var edge in edges) {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -2;
        parent[0] = -1;
        var order = new List<int> { 0 };
        for (int i = 0; i < order.Count; i++) {
            int u = order[i];
            foreach (int v in graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.Add(v);
                }
            }
        }
        const long infinity = 1L << 60;
        var maximum = new long[n][];
        var minimum = new long[n][];
        for (int oi = n - 1; oi >= 0; oi--) {
            int u = order[oi];
            long[] currentMax = new long[k + 1], currentMin = new long[k + 1];
            for (int i = 0; i <= k; i++) { currentMax[i] = -infinity; currentMin[i] = infinity; }
            currentMax[k] = currentMin[k] = nums[u];
            foreach (int v in graph[u]) {
                if (parent[v] != u) continue;
                long[] nextMax = new long[k + 1], nextMin = new long[k + 1];
                for (int i = 0; i <= k; i++) { nextMax[i] = -infinity; nextMin[i] = infinity; }
                for (int first = 0; first <= k; first++) {
                    if (currentMax[first] == -infinity) continue;
                    for (int childDistance = 0; childDistance <= k; childDistance++) {
                        if (maximum[v][childDistance] == -infinity) continue;
                        int second = childDistance + 1;
                        if (second > k) second = k;
                        if (first < k && second < k && first + second < k) continue;
                        int distance = Math.Min(first, second);
                        long maxValue = currentMax[first] + maximum[v][childDistance];
                        long minValue = currentMin[first] + minimum[v][childDistance];
                        nextMax[distance] = Math.Max(nextMax[distance], maxValue);
                        nextMin[distance] = Math.Min(nextMin[distance], minValue);
                    }
                }
                currentMax = nextMax;
                currentMin = nextMin;
            }
            if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
            if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
            maximum[u] = currentMax;
            minimum[u] = currentMin;
        }
        long answer = -(1L << 60);
        foreach (long value in maximum[0]) answer = Math.Max(answer, value);
        return answer;
    }
}
