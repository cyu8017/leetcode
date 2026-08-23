// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

using System.Collections.Generic;

public class MapSum {
    private readonly Dictionary<string, int> values = new();
    private readonly Dictionary<string, int> prefixSums = new();

    public MapSum() {}

    public void Insert(string key, int val) {
        int delta = val - (values.TryGetValue(key, out int old) ? old : 0);
        values[key] = val;
        for (int i = 1; i <= key.Length; ++i) {
            string prefix = key.Substring(0, i);
            prefixSums.TryGetValue(prefix, out int sum);
            prefixSums[prefix] = sum + delta;
        }
    }

    public int Sum(string prefix) {
        return prefixSums.TryGetValue(prefix, out int sum) ? sum : 0;
    }
}
