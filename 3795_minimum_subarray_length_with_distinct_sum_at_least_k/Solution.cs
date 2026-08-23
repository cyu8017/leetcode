// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

using System.Collections.Generic;

public class Solution {
    public int MinLength(int[] nums, int k) {
        int n = nums.Length;
        int ans = n + 1, l = 0;
        var cnt = new Dictionary<int, int>();
        long s = 0;
        for (int r = 0; r < n; r++) {
            if (!cnt.ContainsKey(nums[r])) cnt[nums[r]] = 0;
            if (++cnt[nums[r]] == 1) s += nums[r];
            while (s >= k) {
                if (r - l + 1 < ans) ans = r - l + 1;
                if (--cnt[nums[l]] == 0) s -= nums[l];
                l++;
            }
        }
        return ans > n ? -1 : ans;
    }
}
