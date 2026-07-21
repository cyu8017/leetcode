// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

using System;

public class Solution {
    public int LongestBeautifulSubstring(string word) {
        const string vowels = "aeiou";
        int best = 0;
        for (int start = 0; start < word.Length; start++) {
            if (word[start] != 'a') continue;
            int[] counts = new int[5];
            for (int end = start; end < word.Length; end++) {
                char current = word[end];
                if (end > start && current < word[end - 1]) break;
                int idx = vowels.IndexOf(current);
                if (idx < 0) break;
                counts[idx]++;
                if (idx > 0 && counts[idx - 1] == 0) break;
                bool all = true;
                foreach (int c in counts) if (c == 0) { all = false; break; }
                if (all) best = Math.Max(best, end - start + 1);
            }
        }
        return best;
    }
}
