// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private String[] words;
    private int[] letters;
    private int m, best;
    private final int[] freq = new int[26];
    private List<int[]> bestFreqs;

    public List<List<Integer>> supersequences(String[] words) {
        this.words = words;
        boolean[] used = new boolean[26];
        for (String w : words) {
            used[w.charAt(0) - 'a'] = true;
            used[w.charAt(1) - 'a'] = true;
        }
        List<Integer> lettersList = new ArrayList<>();
        for (int i = 0; i < 26; i++) if (used[i]) lettersList.add(i);
        m = lettersList.size();
        letters = new int[m];
        for (int i = 0; i < m; i++) letters[i] = lettersList.get(i);
        best = 1_000_000_000;
        bestFreqs = new ArrayList<>();
        ArraysFillZero();
        dfs(0);
        List<List<Integer>> res = new ArrayList<>();
        for (int[] f : bestFreqs) {
            List<Integer> row = new ArrayList<>();
            for (int v : f) row.add(v);
            res.add(row);
        }
        return res;
    }

    private void ArraysFillZero() {
        for (int i = 0; i < 26; i++) freq[i] = 0;
    }

    private void dfs(int i) {
        if (i == m) {
            for (String w : words) {
                int a = w.charAt(0) - 'a', b = w.charAt(1) - 'a';
                if (a == b) {
                    if (freq[a] < 2) return;
                } else if (freq[a] < 1 || freq[b] < 1) return;
            }
            int sum = 0;
            int[] f = new int[26];
            for (int j = 0; j < 26; j++) { f[j] = freq[j]; sum += freq[j]; }
            if (sum < best) {
                best = sum;
                bestFreqs = new ArrayList<>();
                bestFreqs.add(f);
            } else if (sum == best) bestFreqs.add(f);
            return;
        }
        int L = letters[i];
        for (int c = 1; c <= 2; c++) {
            freq[L] = c;
            dfs(i + 1);
        }
        freq[L] = 0;
    }
}
