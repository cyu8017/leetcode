// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

using System.Collections.Generic;

public class Solution {
    public int MaxFreq(string s, int maxLetters, int minSize, int maxSize) {
        var counts = new Dictionary<string, int>();
        for (int i = 0; i + minSize <= s.Length; i++) {
            string sub = s.Substring(i, minSize);
            var seen = new HashSet<char>();
            foreach (char ch in sub) seen.Add(ch);
            if (seen.Count <= maxLetters) {
                if (!counts.ContainsKey(sub)) counts[sub] = 0;
                counts[sub]++;
            }
        }
        int best = 0;
        foreach (var kv in counts) best = System.Math.Max(best, kv.Value);
        return best;
    }
}
