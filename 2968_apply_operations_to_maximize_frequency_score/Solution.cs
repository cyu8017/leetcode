// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

using System;

public class Solution {
    public int MaxFrequencyScore(int[] nums, long k) {
        Array.Sort(nums);
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        long Cost(int l, int r) {
            int mid = (l + r) / 2;
            long left = (long)nums[mid] * (mid - l) - (pref[mid] - pref[l]);
            long right = (pref[r + 1] - pref[mid + 1]) - (long)nums[mid] * (r - mid);
            return left + right;
        }
        int ans = 1, left = 0;
        for (int right = 0; right < n; right++) {
            while (Cost(left, right) > k) left++;
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
