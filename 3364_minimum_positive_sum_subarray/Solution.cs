// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

using System.Collections.Generic;

public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int n = nums.Count;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = int.MaxValue;
        bool found = false;
        for (int i = 0; i < n; i++) {
            for (int length = l; length <= r && i + length <= n; length++) {
                int s = pref[i + length] - pref[i];
                if (s > 0 && s < ans) {
                    ans = s;
                    found = true;
                }
            }
        }
        return found ? ans : -1;
    }
}
