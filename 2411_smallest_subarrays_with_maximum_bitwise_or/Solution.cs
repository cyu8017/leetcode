// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

using System;

public class Solution {
    public int[] SmallestSubarrays(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n];
        int[] last = new int[32];
        Array.Fill(last, -1);
        for (int i = n - 1; i >= 0; i--) {
            for (int b = 0; b < 32; b++)
                if (((nums[i] >> b) & 1) != 0) last[b] = i;
            int far = i;
            for (int b = 0; b < 32; b++) far = Math.Max(far, last[b]);
            ans[i] = far - i + 1;
        }
        return ans;
    }
}
