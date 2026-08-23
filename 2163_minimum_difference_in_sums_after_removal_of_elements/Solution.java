// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

import java.util.*;

class Solution {
    public long minimumDifference(int[] nums) {
        int n = nums.length / 3;
        long[] left = new long[nums.length], right = new long[nums.length];
        PriorityQueue<Integer> hmax = new PriorityQueue<>(Collections.reverseOrder());
        long sum = 0;
        for (int i = 0; i < n; i++) { hmax.offer(nums[i]); sum += nums[i]; }
        left[n - 1] = sum;
        for (int i = n; i < 2 * n; i++) {
            hmax.offer(nums[i]);
            sum += nums[i];
            sum -= hmax.poll();
            left[i] = sum;
        }
        PriorityQueue<Integer> hmin = new PriorityQueue<>();
        sum = 0;
        for (int i = nums.length - 1; i >= 2 * n; i--) { hmin.offer(nums[i]); sum += nums[i]; }
        right[2 * n] = sum;
        for (int i = 2 * n - 1; i >= n; i--) {
            hmin.offer(nums[i]);
            sum += nums[i];
            sum -= hmin.poll();
            right[i] = sum;
        }
        long ans = left[n - 1] - right[n];
        for (int i = n; i < 2 * n; i++) ans = Math.min(ans, left[i] - right[i + 1]);
        return ans;
    }
}
