// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

using System.Collections.Generic;

public class Solution {
    public int[] FindNumOfValidWords(string[] words, string[] puzzles) {
        int MaskOf(string s) {
            int mask = 0;
            foreach (char ch in s) mask |= 1 << (ch - 'a');
            return mask;
        }

        var freq = new Dictionary<int, int>();
        foreach (var w in words) {
            int m = MaskOf(w);
            freq[m] = freq.GetValueOrDefault(m) + 1;
        }

        var ans = new int[puzzles.Length];
        for (int i = 0; i < puzzles.Length; i++) {
            string puzzle = puzzles[i];
            int first = 1 << (puzzle[0] - 'a');
            int full = MaskOf(puzzle);
            int sub = full;
            int total = 0;
            while (true) {
                if ((sub & first) != 0) total += freq.GetValueOrDefault(sub);
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans[i] = total;
        }
        return ans;
    }
}
