// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

using System;
using System.Linq;

public class Solution {
    public int MinimumCost(int n, int[][] connections) {
        int[] parent = Enumerable.Range(0, n + 1).ToArray();

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        bool Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) return false;
            parent[rb] = ra;
            return true;
        }

        Array.Sort(connections, (a, b) => a[2].CompareTo(b[2]));
        int cost = 0, edges = 0;
        foreach (var e in connections) {
            if (Unite(e[0], e[1])) {
                cost += e[2];
                if (++edges == n - 1) return cost;
            }
        }
        return -1;
    }
}
