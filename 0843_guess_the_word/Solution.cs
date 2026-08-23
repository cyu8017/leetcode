// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

using System;
using System.Collections.Generic;

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public int Guess(string word);
 * }
 */
public class Solution {
    public void FindSecretWord(string[] words, Master master) {
        int Match(string a, string b) {
            int m = 0;
            for (int i = 0; i < a.Length; i++) if (a[i] == b[i]) m++;
            return m;
        }
        var candidates = new List<string>(words);
        while (candidates.Count > 0) {
            string best = candidates[0];
            int bestWorst = candidates.Count + 1;
            foreach (string w in candidates) {
                int[] buckets = new int[7];
                foreach (string c in candidates) buckets[Match(w, c)]++;
                int worst = 0;
                for (int i = 0; i < 7; i++) worst = Math.Max(worst, buckets[i]);
                if (worst < bestWorst) { bestWorst = worst; best = w; }
            }
            int score = master.Guess(best);
            if (score == 6) return;
            var next = new List<string>();
            foreach (string c in candidates)
                if (Match(c, best) == score) next.Add(c);
            candidates = next;
        }
    }
}
