// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

// JS objDiff stand-in: keys where values differ
using System.Collections.Generic;

public class Solution {
    public SortedDictionary<string, int[]> ObjDiff(SortedDictionary<string, int> obj1, SortedDictionary<string, int> obj2) {
        var diff = new SortedDictionary<string, int[]>();
        foreach (var kv in obj1) {
            if (obj2.TryGetValue(kv.Key, out int v2) && v2 != kv.Value)
                diff[kv.Key] = new int[] { kv.Value, v2 };
        }
        return diff;
    }
}
