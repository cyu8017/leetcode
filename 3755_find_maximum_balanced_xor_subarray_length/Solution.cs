// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxBalancedSubarray(int[] nums) {
        var d = new Dictionary<long, int>();
        int a = 0, b = nums.Length, ans = 0;
        d[b] = -1;
        for (int i = 0; i < nums.Length; i++) {
            a ^= nums[i];
            if (nums[i] % 2 == 0) b++;
            else b--;
            long key = ((long)a << 32) | (uint)b;
            if (d.ContainsKey(key)) ans = Math.Max(ans, i - d[key]);
            else d[key] = i;
        }
        return ans;
    }
}
