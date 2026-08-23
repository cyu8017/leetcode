// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

// JS join-by-id stand-in for maps with int id
using System.Collections.Generic;

public class Solution {
    public IList<SortedDictionary<string, int>> Join(
        IList<SortedDictionary<string, int>> arr1,
        IList<SortedDictionary<string, int>> arr2) {
        var byId = new SortedDictionary<int, SortedDictionary<string, int>>();
        void Merge(IList<SortedDictionary<string, int>> arr) {
            foreach (var obj in arr) {
                int id = obj["id"];
                if (!byId.ContainsKey(id)) byId[id] = new SortedDictionary<string, int>();
                var dest = byId[id];
                foreach (var kv in obj) dest[kv.Key] = kv.Value;
            }
        }
        Merge(arr1); Merge(arr2);
        return new List<SortedDictionary<string, int>>(byId.Values);
    }
}
