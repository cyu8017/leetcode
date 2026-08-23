// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private List<Integer>[] ng;
    private String s;
    private int[] newParent;
    private int[] last;
    private int[] ans;

    private void dfs1(int u) {
        int c = s.charAt(u) - 'a';
        int prev = last[c];
        if (prev != -1) newParent[u] = prev;
        last[c] = u;
        for (int v : g[u]) dfs1(v);
        last[c] = prev;
    }

    private int dfs2(int u) {
        int sz = 1;
        for (int v : ng[u]) sz += dfs2(v);
        return ans[u] = sz;
    }

    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        this.s = s;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[parent[i]].add(i);
        newParent = parent.clone();
        last = new int[26];
        Arrays.fill(last, -1);
        dfs1(0);
        ng = new ArrayList[n];
        for (int i = 0; i < n; i++) ng[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) ng[newParent[i]].add(i);
        ans = new int[n];
        dfs2(0);
        return ans;
    }
}
