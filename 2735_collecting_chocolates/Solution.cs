// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

using System;

public class Solution {
    public long MinCost(int[] nums, int x) {
        int n = nums.Length;
        int[] best = (int[])nums.Clone();
        long ans = 0;
        foreach (int v in nums) ans += v;
        for (int rot = 1; rot < n; rot++) {
            long cur = 1L * rot * x;
            for (int i = 0; i < n; i++) {
                best[i] = Math.Min(best[i], nums[(i + rot) % n]);
                cur += best[i];
            }
            ans = Math.Min(ans, cur);
        }
        return ans;
    }
}
