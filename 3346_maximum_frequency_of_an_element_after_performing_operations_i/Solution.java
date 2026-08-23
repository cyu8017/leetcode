// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        Arrays.sort(nums);
        int n = nums.length;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.merge(x, 1, Integer::sum);
        int ans = 1;
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            int t = e.getKey(), f = e.getValue();
            int lo = lowerBound(nums, t - k);
            int hi = upperBound(nums, t + k);
            int can = hi - lo;
            int use = Math.min(can, f + numOperations);
            if (use > ans) ans = use;
        }
        int l = 0;
        for (int r = 0; r < n; r++) {
            while (nums[r] - nums[l] > 2 * k) l++;
            int window = Math.min(r - l + 1, numOperations);
            if (window > ans) ans = window;
        }
        return ans;
    }

    private static int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
    private static int upperBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
