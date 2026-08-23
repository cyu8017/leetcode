// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int NumSpecialEquivGroups(string[] words) {
        var groups = new HashSet<string>();
        foreach (var w in words) {
            var even = new List<char>();
            var odd = new List<char>();
            for (int i = 0; i < w.Length; i++) {
                if (i % 2 == 0) even.Add(w[i]);
                else odd.Add(w[i]);
            }
            even.Sort();
            odd.Sort();
            groups.Add(new string(even.ToArray()) + "|" + new string(odd.ToArray()));
        }
        return groups.Count;
    }
}
