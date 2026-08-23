// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumSeconds(IList<int> nums) {
        int n = nums.Count;
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!pos.ContainsKey(nums[i])) pos[nums[i]] = new List<int>();
            pos[nums[i]].Add(i);
        }
        int ans = n;
        foreach (var p in pos.Values) {
            int maxGap = 0;
            for (int i = 0; i < p.Count; i++) {
                int gap = (i + 1 < p.Count) ? p[i + 1] - p[i] : p[0] + n - p[i];
                maxGap = Math.Max(maxGap, gap / 2);
            }
            ans = Math.Min(ans, maxGap);
        }
        return ans;
    }
}
