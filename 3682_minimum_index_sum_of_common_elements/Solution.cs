// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumSum(int[] nums1, int[] nums2) {
        const int inf = 1 << 30;
        var d = new Dictionary<int, int>();
        for (int i = 0; i < nums2.Length; i++) {
            if (!d.ContainsKey(nums2[i])) d[nums2[i]] = i;
        }
        int ans = inf;
        for (int i = 0; i < nums1.Length; i++) {
            if (d.TryGetValue(nums1[i], out int j)) ans = Math.Min(ans, i + j);
        }
        return ans == inf ? -1 : ans;
    }
}
