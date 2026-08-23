// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

using System.Collections.Generic;

public class Solution {
    public long MaxSum(int[] nums, int m, int l, int r) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long[] dp = new long[n + 1];
        long bestSelected = -(1L << 62);
        for (int count = 1; count <= m; count++) {
            long[] next = (long[])dp.Clone();
            var deque = new List<int>();
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    long value = dp[addIndex] - prefix[addIndex];
                    while (deque.Count > 0) {
                        int last = deque[deque.Count - 1];
                        if (dp[last] - prefix[last] > value) break;
                        deque.RemoveAt(deque.Count - 1);
                    }
                    deque.Add(addIndex);
                }
                int minIndex = end - r;
                while (deque.Count > 0 && deque[0] < minIndex) deque.RemoveAt(0);
                if (deque.Count > 0) {
                    long candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]];
                    if (candidate > next[end]) next[end] = candidate;
                    if (candidate > bestSelected) bestSelected = candidate;
                }
                if (next[end - 1] > next[end]) next[end] = next[end - 1];
            }
            dp = next;
        }
        return bestSelected;
    }
}
