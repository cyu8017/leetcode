// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxScoreWords(string[] words, char[] letters, int[] score) {
        var available = new Dictionary<char, int>();
        foreach (char ch in letters) available[ch] = available.GetValueOrDefault(ch) + 1;
        var counts = words.Select(w => {
            var c = new Dictionary<char, int>();
            foreach (char ch in w) c[ch] = c.GetValueOrDefault(ch) + 1;
            return c;
        }).ToArray();
        var values = words.Select(w => w.Sum(ch => score[ch - 'a'])).ToArray();

        int Dfs(int i) {
            if (i == words.Length) return 0;
            int best = Dfs(i + 1);
            if (CanUse(counts[i], available)) {
                Apply(counts[i], available, -1);
                best = Math.Max(best, values[i] + Dfs(i + 1));
                Apply(counts[i], available, 1);
            }
            return best;
        }
        return Dfs(0);
    }

    private static bool CanUse(Dictionary<char, int> need, Dictionary<char, int> available) {
        foreach (var kv in need) {
            if (available.GetValueOrDefault(kv.Key) < kv.Value) return false;
        }
        return true;
    }

    private static void Apply(Dictionary<char, int> need, Dictionary<char, int> available, int delta) {
        foreach (var kv in need) available[kv.Key] = available.GetValueOrDefault(kv.Key) + delta * kv.Value;
    }
}
