// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

using System;

public class Solution {
    public int MaxIncreasingGroups(IList<int> usageLimits) {
        int[] arr = new int[usageLimits.Count];
        for (int i = 0; i < usageLimits.Count; i++) arr[i] = usageLimits[i];
        Array.Sort(arr);
        int ans = 0;
        long sum = 0;
        foreach (int v in arr) {
            sum += v;
            long need = 1L * (ans + 1) * (ans + 2) / 2;
            if (sum >= need) ans++;
        }
        return ans;
    }
}
