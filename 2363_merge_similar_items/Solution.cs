// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> MergeSimilarItems(int[][] items1, int[][] items2) {
        var mp = new SortedDictionary<int, int>();
        foreach (var it in items1) {
            if (!mp.ContainsKey(it[0])) mp[it[0]] = 0;
            mp[it[0]] += it[1];
        }
        foreach (var it in items2) {
            if (!mp.ContainsKey(it[0])) mp[it[0]] = 0;
            mp[it[0]] += it[1];
        }
        var ans = new List<IList<int>>();
        foreach (var kv in mp) ans.Add(new List<int> { kv.Key, kv.Value });
        return ans;
    }
}
