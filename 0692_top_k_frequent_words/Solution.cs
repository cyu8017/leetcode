// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

using System.Collections.Generic;

public class Solution {
    public IList<string> TopKFrequent(string[] words, int k) {
        var counts = new Dictionary<string, int>();
        foreach (string word in words) {
            if (!counts.ContainsKey(word)) counts[word] = 0;
            counts[word]++;
        }
        var ordered = new List<string>(counts.Keys);
        ordered.Sort((a, b) => {
            if (counts[a] != counts[b]) return counts[b].CompareTo(counts[a]);
            return string.CompareOrdinal(a, b);
        });
        return ordered.GetRange(0, k);
    }
}
