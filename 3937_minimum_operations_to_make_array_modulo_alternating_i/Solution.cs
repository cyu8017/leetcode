// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

using System;

public class Solution {
    public int MinOperations(int[] nums, int k) {
        for (int i = 0; i < nums.Length; i++) nums[i] %= k;
        int ans = int.MaxValue;
        for (int x = 0; x < k; x++) {
            for (int y = 0; y < k; y++) {
                if (x == y) continue;
                int cnt = 0;
                for (int i = 0; i < nums.Length; i++) {
                    int target = (i & 1) != 0 ? y : x;
                    int diff = Math.Abs(target - nums[i]);
                    cnt += Math.Min(diff, k - diff);
                }
                ans = Math.Min(ans, cnt);
            }
        }
        return ans;
    }
}
