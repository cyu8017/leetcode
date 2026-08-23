// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

using System;
using System.Collections.Generic;

public class Solution {
    public int ShortestSubarray(int[] nums, int k) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        var dq = new LinkedList<int>();
        int ans = n + 1;
        for (int i = 0; i <= n; i++) {
            while (dq.Count > 0 && prefix[i] - prefix[dq.First.Value] >= k) {
                ans = Math.Min(ans, i - dq.First.Value);
                dq.RemoveFirst();
            }
            while (dq.Count > 0 && prefix[i] <= prefix[dq.Last.Value]) dq.RemoveLast();
            dq.AddLast(i);
        }
        return ans <= n ? ans : -1;
    }
}
