// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

using System;

public class Solution {
    public int MinChanges(int[] nums, int k) {
        int[] d = new int[k + 2];
        int n = nums.Length;
        for (int i = 0; i < n / 2; i++) {
            int x = nums[i], y = nums[n - 1 - i];
            if (x > y) { int t = x; x = y; y = t; }
            d[0] += 1;
            d[y - x] -= 1;
            d[y - x + 1] += 1;
            int mx = Math.Max(y, k - x);
            d[mx + 1] -= 1;
            d[mx + 1] += 2;
        }
        int ans = n, s = 0;
        foreach (int x in d) {
            s += x;
            ans = Math.Min(ans, s);
        }
        return ans;
    }
}
