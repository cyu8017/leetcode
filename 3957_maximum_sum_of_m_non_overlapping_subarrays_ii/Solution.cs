// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

using System.Collections.Generic;

public class Solution {
    private struct State {
        public long Value;
        public int Count;
        public State(long value, int count) { Value = value; Count = count; }
    }

    private static bool Better(State a, State b) {
        return a.Value > b.Value || (a.Value == b.Value && a.Count > b.Count);
    }

    public long MaxSum(int[] nums, int m, int l, int r) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        State Run(long penalty) {
            State[] dp = new State[n + 1];
            var deque = new List<int>();
            bool CandidateBetter(int a, int b) {
                State left = new State(dp[a].Value - prefix[a], dp[a].Count);
                State right = new State(dp[b].Value - prefix[b], dp[b].Count);
                return Better(left, right);
            }
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    while (deque.Count > 0 && CandidateBetter(addIndex, deque[deque.Count - 1])) deque.RemoveAt(deque.Count - 1);
                    deque.Add(addIndex);
                }
                int minIndex = end - r;
                while (deque.Count > 0 && deque[0] < minIndex) deque.RemoveAt(0);
                dp[end] = dp[end - 1];
                if (deque.Count > 0) {
                    int start = deque[0];
                    State take = new State(dp[start].Value + prefix[end] - prefix[start] - penalty, dp[start].Count + 1);
                    if (Better(take, dp[end])) dp[end] = take;
                }
            }
            return dp[n];
        }

        State unconstrained = Run(0);
        if (unconstrained.Count > 0 && unconstrained.Count <= m) return unconstrained.Value;
        if (unconstrained.Count > m) {
            long bound = 0;
            foreach (int value in nums) bound += value >= 0 ? value : -value;
            long low = 0, high = bound + 1;
            while (low < high) {
                long mid = low + (high - low + 1) / 2;
                if (Run(mid).Count >= m) low = mid;
                else high = mid - 1;
            }
            State state = Run(low);
            return state.Value + low * m;
        }
        const long infinity = 1L << 60;
        long bestSingle = -infinity;
        var dq = new List<int>();
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                while (dq.Count > 0 && prefix[dq[dq.Count - 1]] >= prefix[addIndex]) dq.RemoveAt(dq.Count - 1);
                dq.Add(addIndex);
            }
            int minIndex = end - r;
            while (dq.Count > 0 && dq[0] < minIndex) dq.RemoveAt(0);
            if (dq.Count > 0) {
                long sum = prefix[end] - prefix[dq[0]];
                if (sum > bestSingle) bestSingle = sum;
            }
        }
        return bestSingle;
    }
}
