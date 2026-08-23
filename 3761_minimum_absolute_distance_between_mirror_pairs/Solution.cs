// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinMirrorPairDistance(int[] nums) {
        int n = nums.Length;
        var pos = new Dictionary<int, int>();
        int ans = n + 1;
        int Reverse(int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        }
        for (int i = 0; i < n; i++) {
            if (pos.ContainsKey(nums[i])) ans = Math.Min(ans, i - pos[nums[i]]);
            pos[Reverse(nums[i])] = i;
        }
        return ans > n ? -1 : ans;
    }
}
