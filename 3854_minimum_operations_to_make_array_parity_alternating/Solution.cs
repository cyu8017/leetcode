// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

using System;

public class Solution {
    public int[] MakeParityAlternating(int[] nums) {
        if (nums.Length == 1) return new int[] { 0, 0 };
        int mn = nums[0], mx = nums[0];
        foreach (int x in nums) { mn = Math.Min(mn, x); mx = Math.Max(mx, x); }
        int[] F(int k) {
            int cnt = 0, a = int.MaxValue, b = int.MinValue;
            for (int i = 0; i < nums.Length; i++) {
                int x = nums[i];
                if (((x - i) & 1) != k) {
                    cnt++;
                    if (x == mn) x++;
                    else if (x == mx) x--;
                }
                a = Math.Min(a, x);
                b = Math.Max(b, x);
            }
            return new int[] { cnt, Math.Max(1, b - a) };
        }
        var r0 = F(0);
        var r1 = F(1);
        if (r0[0] != r1[0]) return r0[0] < r1[0] ? r0 : r1;
        return r0[1] <= r1[1] ? r0 : r1;
    }
}
