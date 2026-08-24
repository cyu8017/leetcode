// CONFIG class=Solution method=maxSum types=None
// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long maxSum(int[] nums, int m, int l, int r) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long[] dp = new long[n + 1];
        long bestSelected = -(1L << 62);
        for (int count = 1; count <= m; count++) {
            long[] next = dp.clone();
            var deque = new ArrayList<Integer>();
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    long value = dp[addIndex] - prefix[addIndex];
                    while (deque.size() > 0) {
                        int last = deque.get(deque.size() - 1);
                        if (dp[last] - prefix[last] > value) break;
                        deque.remove(deque.size() - 1);
                    }
                    deque.add(addIndex);
                }
                int minIndex = end - r;
                while (deque.size() > 0 && deque.get(0) < minIndex) deque.remove(0);
                if (deque.size() > 0) {
                    long candidate = prefix[end] + dp[deque.get(0)] - prefix[deque.get(0)];
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
