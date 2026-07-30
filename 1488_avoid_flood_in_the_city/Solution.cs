// LeetCode 1488 - Avoid Flood In The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

using System.Collections.Generic;
public class Solution {
    public int[] AvoidFlood(int[] rains) {
        var ans = new int[rains.Length];
        for (int i = 0; i < ans.Length; i++) ans[i] = -1;
        var full = new Dictionary<int, int>();
        var dry = new List<int>();
        for (int i = 0; i < rains.Length; i++) {
            int lake = rains[i];
            if (lake == 0) { dry.Add(i); ans[i] = 1; }
            else {
                if (full.ContainsKey(lake)) {
                    int j = dry.BinarySearch(full[lake]);
                    if (j < 0) j = ~j;
                    if (j == dry.Count) return System.Array.Empty<int>();
                    ans[dry[j]] = lake; dry.RemoveAt(j);
                }
                full[lake] = i;
            }
        }
        return ans;
    }
}
