// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum_cost_to_merge_sorted_lists/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long minMergeCost(int[][] lists) {
        int m = lists.length;
        int totalMasks = 1 << m;
        List<Integer>[] merged = newList(totalMasks);
        int[] length = new int[totalMasks], median = new int[totalMasks];
        for (int mask = 1; mask < totalMasks; mask++) {
            int bit = mask & -mask;
            int index = Integer.numberOfTrailingZeros(bit);
            List<Integer> previous = merged[mask ^ bit];
            int[] current = lists[index];
            List<Integer> out = new ArrayList<>(previous.size() + current.length);
            int i = 0, j = 0;
            while (i < previous.size() || j < current.length) {
                if (j == current.length || (i < previous.size() && previous.get(i) <= current[j])) {
                    out.add(previous.get(i++));
                } else {
                    out.add(current[j++]);
                }
            }
            merged[mask] = out;
            length[mask] = out.size();
            median[mask] = out.get((out.size() - 1) / 2);
        }
        final long INF = 1L << 62;
        long[] dp = new long[totalMasks];
        for (int mask = 1; mask < totalMasks; mask++) {
            if ((mask & (mask - 1)) == 0) continue;
            dp[mask] = INF;
            int firstBit = mask & -mask;
            for (int left = (mask - 1) & mask; left > 0; left = (left - 1) & mask) {
                if ((left & firstBit) == 0) continue;
                int right = mask ^ left;
                if (right == 0) continue;
                int diff = median[left] - median[right];
                if (diff < 0) diff = -diff;
                long candidate = dp[left] + dp[right] + length[mask] + diff;
                if (candidate < dp[mask]) dp[mask] = candidate;
            }
        }
        return dp[totalMasks - 1];
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
