// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

import java.util.Arrays;

class Solution {
    private long cost(int[] nums, long[] pref, int l, int r) {
        int mid = (l + r) / 2;
        long left = (long) nums[mid] * (mid - l) - (pref[mid] - pref[l]);
        long right = (pref[r + 1] - pref[mid + 1]) - (long) nums[mid] * (r - mid);
        return left + right;
    }

    public int maxFrequencyScore(int[] nums, long k) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = 1, left = 0;
        for (int right = 0; right < n; right++) {
            while (cost(nums, pref, left, right) > k) left++;
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
