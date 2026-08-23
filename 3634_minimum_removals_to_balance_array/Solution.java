// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

import java.util.Arrays;

class Solution {
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length, cnt = 0;
        for (int i = 0; i < n; i++) {
            int j = n;
            if (1L * nums[i] * k <= nums[n - 1]) {
                long target = 1L * nums[i] * k + 1;
                j = lowerBound(nums, target);
            }
            cnt = Math.max(cnt, j - i);
        }
        return n - cnt;
    }

    private static int lowerBound(int[] a, long target) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
