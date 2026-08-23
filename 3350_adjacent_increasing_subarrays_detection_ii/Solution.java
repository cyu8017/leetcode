// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

import java.util.List;

class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int n = nums.size();
        int[] up = new int[n];
        up[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            up[i] = (nums.get(i) < nums.get(i + 1)) ? up[i + 1] + 1 : 1;
        }
        int lo = 1, hi = n / 2;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(up, n, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean ok(int[] up, int n, int k) {
        for (int i = 0; i + 2 * k <= n; i++) {
            if (up[i] >= k && up[i + k] >= k) return true;
        }
        return false;
    }
}
