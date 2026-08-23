// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

using System.Collections.Generic;

public class Solution {
    public long MinMergeCost(int[][] lists) {
        int m = lists.Length;
        int totalMasks = 1 << m;
        var merged = new List<int>[totalMasks];
        for (int i = 0; i < totalMasks; i++) merged[i] = new List<int>();
        int[] length = new int[totalMasks], median = new int[totalMasks];
        for (int mask = 1; mask < totalMasks; mask++) {
            int bit = mask & -mask;
            int index = 0;
            while ((1 << index) != bit) index++;
            var previous = merged[mask ^ bit];
            var current = lists[index];
            var outList = new List<int>(previous.Count + current.Length);
            int i = 0, j = 0;
            while (i < previous.Count || j < current.Length) {
                if (j == current.Length || (i < previous.Count && previous[i] <= current[j])) {
                    outList.Add(previous[i++]);
                } else {
                    outList.Add(current[j++]);
                }
            }
            merged[mask] = outList;
            length[mask] = outList.Count;
            median[mask] = outList[(outList.Count - 1) / 2];
        }
        const long INF = 1L << 62;
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
}
