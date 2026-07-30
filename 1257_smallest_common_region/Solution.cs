// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

using System.Collections.Generic;

public class Solution {
    public string FindSmallestRegion(string[][] regions, string region1, string region2) {
        var parent = new Dictionary<string, string>();
        foreach (var group in regions) {
            for (int i = 1; i < group.Length; i++) parent[group[i]] = group[0];
        }
        var ancestors = new HashSet<string>();
        while (!string.IsNullOrEmpty(region1)) {
            ancestors.Add(region1);
            parent.TryGetValue(region1, out region1);
        }
        while (!ancestors.Contains(region2)) {
            parent.TryGetValue(region2, out region2);
        }
        return region2;
    }
}
