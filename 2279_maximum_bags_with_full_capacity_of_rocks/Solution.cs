// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

using System;

public class Solution {
    public int MaximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int[] need = new int[capacity.Length];
        for (int i = 0; i < capacity.Length; i++) need[i] = capacity[i] - rocks[i];
        Array.Sort(need);
        int ans = 0;
        foreach (int n in need) {
            if (additionalRocks < n) break;
            additionalRocks -= n;
            ans++;
        }
        return ans;
    }
}
