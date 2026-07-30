// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> MostVisitedPattern(string[] username, int[] timestamp, string[] website) {
        var visits = new Dictionary<string, List<(int t, string site)>>();
        for (int i = 0; i < username.Length; i++) {
            if (!visits.ContainsKey(username[i])) visits[username[i]] = new List<(int, string)>();
            visits[username[i]].Add((timestamp[i], website[i]));
        }
        var scores = new SortedDictionary<(string, string, string), int>();
        foreach (var list in visits.Values) {
            list.Sort((a, b) => a.t.CompareTo(b.t));
            var sites = list.Select(x => x.site).ToList();
            var patterns = new HashSet<(string, string, string)>();
            int m = sites.Count;
            for (int i = 0; i < m; i++)
                for (int j = i + 1; j < m; j++)
                    for (int k = j + 1; k < m; k++)
                        patterns.Add((sites[i], sites[j], sites[k]));
            foreach (var p in patterns) {
                if (!scores.ContainsKey(p)) scores[p] = 0;
                scores[p]++;
            }
        }
        (string, string, string) best = default;
        int bestCount = -1;
        foreach (var kv in scores) {
            if (kv.Value > bestCount || (kv.Value == bestCount && Comparer<(string, string, string)>.Default.Compare(kv.Key, best) < 0)) {
                bestCount = kv.Value;
                best = kv.Key;
            }
        }
        return new List<string> { best.Item1, best.Item2, best.Item3 };
    }
}
