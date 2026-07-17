// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] SortFeatures(string[] features, string[] responses) {
        var featureSet = new HashSet<string>(features);
        var count = new Dictionary<string, int>();
        foreach (var response in responses) {
            var seen = new HashSet<string>();
            foreach (var word in response.Split(' ', StringSplitOptions.RemoveEmptyEntries)) {
                if (featureSet.Contains(word)) {
                    seen.Add(word);
                }
            }
            foreach (var word in seen) {
                count[word] = count.TryGetValue(word, out var c) ? c + 1 : 1;
            }
        }
        return features
            .OrderByDescending(f => count.TryGetValue(f, out var c) ? c : 0)
            .ThenBy(f => f, StringComparer.Ordinal)
            .ToArray();
    }
}
