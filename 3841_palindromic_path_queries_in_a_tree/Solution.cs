// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public bool[] PalindromicPathQueries(int n, int[][] edges, string s, string[] queries) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var edge in edges) {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }
        var parent = new int[n];
        var depth = new int[n];
        Array.Fill(parent, -2);
        parent[0] = -1;
        var order = new List<int> { 0 };
        for (int i = 0; i < order.Count; i++) {
            int u = order[i];
            foreach (int v in graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    order.Add(v);
                }
            }
        }
        var size = new int[n];
        var heavy = new int[n];
        Array.Fill(heavy, -1);
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            size[u] = 1;
            foreach (int v in graph[u]) {
                if (parent[v] == u) {
                    size[u] += size[v];
                    if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v;
                }
            }
        }
        var head = new int[n];
        var position = new int[n];
        var stack = new List<(int node, int h)> { (0, 0) };
        int nextPosition = 0;
        while (stack.Count > 0) {
            var chain = stack[stack.Count - 1];
            stack.RemoveAt(stack.Count - 1);
            for (int u = chain.node; u != -1; u = heavy[u]) {
                head[u] = chain.h;
                position[u] = nextPosition++;
                foreach (int v in graph[u]) {
                    if (parent[v] == u && v != heavy[u]) stack.Add((v, v));
                }
            }
        }
        var bit = new int[n + 1];
        void Update(int index, int value) {
            for (index++; index <= n; index += index & -index) bit[index] ^= value;
        }
        int Prefix(int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result ^= bit[index];
            return result;
        }
        int PathMask(int u, int v) {
            int result = 0;
            while (head[u] != head[v]) {
                if (depth[head[u]] < depth[head[v]]) { int tmp = u; u = v; v = tmp; }
                result ^= Prefix(position[u] + 1) ^ Prefix(position[head[u]]);
                u = parent[head[u]];
            }
            if (position[u] > position[v]) { int tmp = u; u = v; v = tmp; }
            return result ^ Prefix(position[v] + 1) ^ Prefix(position[u]);
        }
        var current = s.ToCharArray();
        for (int node = 0; node < n; node++) Update(position[node], 1 << (current[node] - 'a'));
        var answer = new List<bool>();
        foreach (var query in queries) {
            var parts = query.Split(' ');
            string op = parts[0];
            int node = int.Parse(parts[1]);
            if (op == "update") {
                char newCharacter = parts[2][0];
                int delta = (1 << (current[node] - 'a')) ^ (1 << (newCharacter - 'a'));
                Update(position[node], delta);
                current[node] = newCharacter;
            } else {
                int other = int.Parse(parts[2]);
                int mask = PathMask(node, other);
                answer.Add((mask & (mask - 1)) == 0);
            }
        }
        return answer.ToArray();
    }
}
