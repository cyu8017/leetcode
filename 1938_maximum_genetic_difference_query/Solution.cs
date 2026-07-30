// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

using System.Collections.Generic;

public class Solution {
    class TrieNode {
        public TrieNode[] Child = new TrieNode[2];
        public int Cnt;
    }

    const int BITS = 17;
    TrieNode trieRoot;
    List<int>[] children;
    List<(int qi, int val)>[] qmap;
    int[] ans;

    public int[] MaxGeneticDifference(int[] parents, int[][] queries) {
        int n = parents.Length;
        children = new List<int>[n];
        qmap = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) {
            children[i] = new List<int>();
            qmap[i] = new List<(int, int)>();
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (parents[i] == -1) root = i;
            else children[parents[i]].Add(i);
        }
        for (int i = 0; i < queries.Length; i++)
            qmap[queries[i][0]].Add((i, queries[i][1]));
        ans = new int[queries.Length];
        trieRoot = new TrieNode();
        Dfs(root);
        return ans;
    }

    void TrieUpdate(int num, int delta) {
        var node = trieRoot;
        for (int b = BITS; b >= 0; b--) {
            int bit = (num >> b) & 1;
            if (node.Child[bit] == null) node.Child[bit] = new TrieNode();
            node = node.Child[bit];
            node.Cnt += delta;
        }
    }

    int TrieMaxXor(int num) {
        var node = trieRoot;
        int res = 0;
        for (int b = BITS; b >= 0; b--) {
            int bit = (num >> b) & 1;
            int want = 1 - bit;
            if (node.Child[want] != null && node.Child[want].Cnt > 0) {
                res |= 1 << b;
                node = node.Child[want];
            } else node = node.Child[bit];
        }
        return res;
    }

    void Dfs(int u) {
        TrieUpdate(u, 1);
        foreach (var (qi, val) in qmap[u]) ans[qi] = TrieMaxXor(val);
        foreach (int v in children[u]) Dfs(v);
        TrieUpdate(u, -1);
    }
}