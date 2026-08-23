// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

using System.Collections.Generic;

public class Solution {
    public int SimilarPairs(string[] words) {
        var freq = new Dictionary<int, int>();
        int ans = 0;
        foreach (string w in words) {
            int mask = 0;
            foreach (char c in w) mask |= 1 << (c - 'a');
            if (freq.ContainsKey(mask)) ans += freq[mask];
            if (!freq.ContainsKey(mask)) freq[mask] = 0;
            freq[mask]++;
        }
        return ans;
    }
}
