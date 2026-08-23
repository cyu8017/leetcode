// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private long ans;
    private Map<Integer, Integer> freq;
    private List<Integer>[] g;
    private String s;

    public long countPalindromePaths(List<Integer> parent, String s) {
        int n = parent.size();
        this.s = s;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[parent.get(i)].add(i);
        freq = new HashMap<>();
        freq.put(0, 1);
        ans = 0;
        dfs(0, 0);
        return ans;
    }

    private void dfs(int u, int mask) {
        for (int v : g[u]) {
            int nm = mask ^ (1 << (s.charAt(v) - 'a'));
            ans += freq.getOrDefault(nm, 0);
            for (int b = 0; b < 26; b++) {
                ans += freq.getOrDefault(nm ^ (1 << b), 0);
            }
            freq.put(nm, freq.getOrDefault(nm, 0) + 1);
            dfs(v, nm);
        }
    }
}
