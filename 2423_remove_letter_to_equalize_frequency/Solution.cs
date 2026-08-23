// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

using System.Collections.Generic;

public class Solution {
    public bool EqualFrequency(string word) {
        for (int skip = 0; skip < word.Length; skip++) {
            int[] cnt = new int[26];
            for (int i = 0; i < word.Length; i++) {
                if (i == skip) continue;
                cnt[word[i] - 'a']++;
            }
            var freq = new Dictionary<int, int>();
            foreach (int c in cnt) {
                if (c > 0) {
                    if (!freq.ContainsKey(c)) freq[c] = 0;
                    freq[c]++;
                }
            }
            if (freq.Count == 1) return true;
        }
        return false;
    }
}
