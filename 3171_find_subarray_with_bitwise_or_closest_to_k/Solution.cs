// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

using System;

public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        int mx = 0;
        foreach (int v in nums) mx = Math.Max(mx, v);
        int m = mx == 0 ? 1 : 32 - LeadingZeroCount(mx);
        int[] cnt = new int[m];
        int ans = int.MaxValue, s = 0, i = 0;
        for (int j = 0; j < nums.Length; j++) {
            int x = nums[j];
            s |= x;
            ans = Math.Min(ans, Math.Abs(s - k));
            for (int h = 0; h < m; h++) if (((x >> h) & 1) != 0) cnt[h]++;
            while (i < j && s > k) {
                int y = nums[i];
                for (int h = 0; h < m; h++) {
                    if (((y >> h) & 1) != 0) {
                        if (--cnt[h] == 0) s ^= 1 << h;
                    }
                }
                ans = Math.Min(ans, Math.Abs(s - k));
                i++;
            }
        }
        return ans;
    }

    static int LeadingZeroCount(int x) {
        if (x == 0) return 32;
        int n = 0;
        for (int bit = 31; bit >= 0; bit--) {
            if (((x >> bit) & 1) != 0) break;
            n++;
        }
        return n;
    }
}
