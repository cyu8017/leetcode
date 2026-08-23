// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

using System;

public class Solution {
    public long MinPartitionScore(int[] nums, int k) {
        int n = nums.Length;
        var prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long Value(int left, int right) {
            long sum = prefix[right] - prefix[left];
            return sum * (sum + 1) / 2;
        }
        const long INF = 1L << 62;
        var previous = new long[n + 1];
        Array.Fill(previous, INF);
        previous[0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            var current = new long[n + 1];
            Array.Fill(current, INF);
            void Compute(int lo, int hi, int optLo, int optHi) {
                if (lo > hi) return;
                int mid = (lo + hi) / 2;
                int bestIndex = -1;
                int end = Math.Min(optHi, mid - 1);
                for (int split = optLo; split <= end; split++) {
                    if (previous[split] == INF) continue;
                    long candidate = previous[split] + Value(split, mid);
                    if (candidate < current[mid]) {
                        current[mid] = candidate;
                        bestIndex = split;
                    }
                }
                if (bestIndex == -1) bestIndex = optLo;
                Compute(lo, mid - 1, optLo, bestIndex);
                Compute(mid + 1, hi, bestIndex, optHi);
            }
            Compute(parts, n, parts - 1, n - 1);
            previous = current;
        }
        return previous[n];
    }
}
