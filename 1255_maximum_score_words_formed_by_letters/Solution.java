// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

import java.util.*;

class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int[] available = new int[26];
        for (char ch : letters) available[ch - 'a']++;
        int[][] counts = new int[words.length][26];
        int[] values = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (char ch : words[i].toCharArray()) counts[i][ch - 'a']++;
            for (char ch : words[i].toCharArray()) values[i] += score[ch - 'a'];
        }
        return dfs(0, words.length, counts, values, available);
    }

    private int dfs(int i, int n, int[][] counts, int[] values, int[] available) {
        if (i == n) return 0;
        int best = dfs(i + 1, n, counts, values, available);
        if (canUse(counts[i], available)) {
            apply(counts[i], available, -1);
            best = Math.max(best, values[i] + dfs(i + 1, n, counts, values, available));
            apply(counts[i], available, 1);
        }
        return best;
    }

    private boolean canUse(int[] need, int[] available) {
        for (int j = 0; j < 26; j++) if (need[j] > available[j]) return false;
        return true;
    }

    private void apply(int[] need, int[] available, int sign) {
        for (int j = 0; j < 26; j++) available[j] += sign * need[j];
    }
}

