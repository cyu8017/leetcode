// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

using System;

public class Solution {
    public int MinMoves(int[] nums, int limit) {
        int n = nums.Length;
        int[] d = new int[2 * limit + 2];
        for (int i = 0; i < n / 2; i++) {
            int a = nums[i], b = nums[n - 1 - i];
            int lo = Math.Min(a, b) + 1;
            int hi = Math.Max(a, b) + limit;
            int s = a + b;
            d[2] += 2;
            d[lo] -= 1;
            d[s] -= 1;
            d[s + 1] += 1;
            d[hi + 1] += 1;
        }
        int ans = int.MaxValue, cur = 0;
        for (int s = 2; s <= 2 * limit; s++) {
            cur += d[s];
            ans = Math.Min(ans, cur);
        }
        return ans;
    }
}
