// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] child = new TrieNode[2];
        int cnt;
    }

    static final int BITS = 17;
    List<Integer>[] children;
    List<int[]>[] qmap;
    int[] ans;
    TrieNode trie = new TrieNode();

    public int[] maxGeneticDifference(int[] parents, int[][] queries) {
        int n = parents.length;
        children = new ArrayList[n];
        qmap = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            children[i] = new ArrayList<>();
            qmap[i] = new ArrayList<>();
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (parents[i] == -1) root = i;
            else children[parents[i]].add(i);
        }
        ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) qmap[queries[i][0]].add(new int[]{i, queries[i][1]});
        dfs(root);
        return ans;
    }

    private void dfs(int u) {
        update(u, 1);
        for (int[] q : qmap[u]) ans[q[0]] = maxXor(q[1]);
        for (int v : children[u]) dfs(v);
        update(u, -1);
    }

    private void update(int num, int delta) {
        TrieNode node = trie;
        for (int b = BITS; b >= 0; b--) {
            int bit = (num >> b) & 1;
            if (node.child[bit] == null) node.child[bit] = new TrieNode();
            node = node.child[bit];
            node.cnt += delta;
        }
    }

    private int maxXor(int num) {
        TrieNode node = trie;
        int res = 0;
        for (int b = BITS; b >= 0; b--) {
            int bit = (num >> b) & 1, want = 1 - bit;
            if (node.child[want] != null && node.child[want].cnt > 0) {
                res |= 1 << b;
                node = node.child[want];
            } else {
                node = node.child[bit];
            }
        }
        return res;
    }
}
