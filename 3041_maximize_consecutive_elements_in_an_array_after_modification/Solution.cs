// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSelectedElements(int[] nums) {
        Array.Sort(nums);
        var dp = new Dictionary<int, int>();
        int ans = 0;
        foreach (int num in nums) {
            dp.TryGetValue(num, out int dn);
            dp.TryGetValue(num - 1, out int dnm1);
            dp[num + 1] = dn + 1;
            dp[num] = dnm1 + 1;
            ans = Math.Max(ans, Math.Max(dp[num], dp[num + 1]));
        }
        return ans;
    }
}
