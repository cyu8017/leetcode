// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private String s;
    private boolean[] ans;

    private boolean isPal(String t) {
        for (int i = 0, j = t.length() - 1; i < j; i++, j--) {
            if (t.charAt(i) != t.charAt(j)) return false;
        }
        return true;
    }

    private String dfsStr(int u) {
        StringBuilder out = new StringBuilder();
        for (int v : g[u]) out.append(dfsStr(v));
        out.append(s.charAt(u));
        ans[u] = isPal(out.toString());
        return out.toString();
    }

    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        this.s = s;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[parent[i]].add(i);
        ans = new boolean[n];
        dfsStr(0);
        return ans;
    }
}
