// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

// JS immutability helper stand-in
using System;
using System.Collections.Generic;

public class Solution {
    public IList<SortedDictionary<string, int>> ImmutableHelper(
        SortedDictionary<string, int> obj,
        IList<Action<SortedDictionary<string, int>>> mutators) {
        var outList = new List<SortedDictionary<string, int>>();
        foreach (var m in mutators) {
            var copy = new SortedDictionary<string, int>(obj);
            m(copy);
            outList.Add(copy);
        }
        return outList;
    }
}
