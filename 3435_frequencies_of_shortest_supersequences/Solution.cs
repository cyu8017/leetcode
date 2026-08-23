// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> Supersequences(string[] words) {
        bool[] used = new bool[26];
        foreach (string w in words) {
            used[w[0] - 'a'] = true;
            used[w[1] - 'a'] = true;
        }
        var letters = new List<int>();
        for (int i = 0; i < 26; i++) if (used[i]) letters.Add(i);
        int m = letters.Count;
        int best = 1000000000;
        var bestFreqs = new List<IList<int>>();
        int[] freq = new int[26];
        void Dfs(int i) {
            if (i == m) {
                bool ok = true;
                foreach (string w in words) {
                    int a = w[0] - 'a', b = w[1] - 'a';
                    if (a == b) {
                        if (freq[a] < 2) { ok = false; break; }
                    } else if (freq[a] < 1 || freq[b] < 1) { ok = false; break; }
                }
                if (!ok) return;
                int sum = 0;
                var f = new int[26];
                for (int j = 0; j < 26; j++) { f[j] = freq[j]; sum += freq[j]; }
                if (sum < best) {
                    best = sum;
                    bestFreqs = new List<IList<int>> { f };
                } else if (sum == best) bestFreqs.Add(f);
                return;
            }
            int L = letters[i];
            for (int c = 1; c <= 2; c++) {
                freq[L] = c;
                Dfs(i + 1);
            }
            freq[L] = 0;
        }
        Dfs(0);
        return bestFreqs;
    }
}
