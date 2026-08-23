// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

import java.util.TreeMap;

class Solution {
    String[] words;
    int n;
    TreeMap<Integer, Integer> tm = new TreeMap<>();

    int calc(String s, String t) {
        int m = Math.min(s.length(), t.length());
        for (int k = 0; k < m; k++) if (s.charAt(k) != t.charAt(k)) return k;
        return m;
    }

    void add(int i, int j) {
        if (i >= 0 && i < n && j >= 0 && j < n) tm.merge(calc(words[i], words[j]), 1, Integer::sum);
    }

    void remove(int i, int j) {
        if (i >= 0 && i < n && j >= 0 && j < n) {
            int x = calc(words[i], words[j]);
            int c = tm.get(x);
            if (c == 1) tm.remove(x);
            else tm.put(x, c - 1);
        }
    }

    public int[] longestCommonPrefix(String[] words) {
        this.words = words;
        n = words.length;
        for (int i = 0; i + 1 < n; i++) add(i, i + 1);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            remove(i, i + 1);
            remove(i - 1, i);
            add(i - 1, i + 1);
            if (!tm.isEmpty() && tm.lastKey() > 0) ans[i] = tm.lastKey();
            remove(i - 1, i + 1);
            add(i - 1, i);
            add(i, i + 1);
        }
        return ans;
    }
}
