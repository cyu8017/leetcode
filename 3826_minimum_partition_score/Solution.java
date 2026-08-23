// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum_partition_score/

import java.util.Arrays;

class Solution {
    private long[] prefix;
    private long[] previous;
    private long[] current;
    private static final long INF = 1L << 62;

    public long minPartitionScore(int[] nums, int k) {
        int n = nums.length;
        prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        previous = new long[n + 1];
        Arrays.fill(previous, INF);
        previous[0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            current = new long[n + 1];
            Arrays.fill(current, INF);
            compute(parts, n, parts - 1, n - 1);
            previous = current;
        }
        return previous[n];
    }

    private long value(int left, int right) {
        long sum = prefix[right] - prefix[left];
        return sum * (sum + 1) / 2;
    }

    private void compute(int lo, int hi, int optLo, int optHi) {
        if (lo > hi) return;
        int mid = (lo + hi) / 2;
        int bestIndex = -1;
        int end = Math.min(optHi, mid - 1);
        for (int split = optLo; split <= end; split++) {
            if (previous[split] == INF) continue;
            long candidate = previous[split] + value(split, mid);
            if (candidate < current[mid]) {
                current[mid] = candidate;
                bestIndex = split;
            }
        }
        if (bestIndex == -1) bestIndex = optLo;
        compute(lo, mid - 1, optLo, bestIndex);
        compute(mid + 1, hi, bestIndex, optHi);
    }
}
