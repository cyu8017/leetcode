// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

import java.util.Arrays;

class Solution {
    private long[] cost;
    private static final long INF = 1L << 60;

    public long minOperations(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) return 0;
        if (k > n / 2) return -1;
        cost = new long[n];
        for (int i = 0; i < n; i++) {
            int left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
            int need = Math.max(left, right);
            if (need >= nums[i]) cost[i] = (long) need - nums[i] + 1;
        }
        long answer = line(1, n - 1, k);
        long withFirst = line(2, n - 2, k - 1);
        if (withFirst != INF) {
            withFirst += cost[0];
            answer = Math.min(answer, withFirst);
        }
        if (answer == INF) return -1;
        return answer;
    }

    private long line(int left, int right, int choose) {
        if (choose == 0) return 0;
        if (left > right || choose > (right - left + 2) / 2) return INF;
        long[] prev2 = new long[choose + 1];
        long[] prev1 = new long[choose + 1];
        Arrays.fill(prev2, INF);
        Arrays.fill(prev1, INF);
        prev2[0] = prev1[0] = 0;
        for (int i = left; i <= right; i++) {
            long[] current = prev1.clone();
            for (int j = 1; j <= choose; j++) {
                if (prev2[j - 1] != INF && prev2[j - 1] + cost[i] < current[j]) {
                    current[j] = prev2[j - 1] + cost[i];
                }
            }
            prev2 = prev1;
            prev1 = current;
        }
        return prev1[choose];
    }
}
