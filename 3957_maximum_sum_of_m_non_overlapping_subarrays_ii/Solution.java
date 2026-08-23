// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static class State {
        long value;
        int count;
        State() {}
        State(long value, int count) { this.value = value; this.count = count; }
    }

    private static boolean better(State a, State b) {
        return a.value > b.value || (a.value == b.value && a.count > b.count);
    }

    public long maxSum(int[] nums, int m, int l, int r) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        State unconstrained = run(prefix, n, l, r, 0);
        if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value;
        if (unconstrained.count > m) {
            long bound = 0;
            for (int value : nums) bound += value >= 0 ? value : -value;
            long low = 0, high = bound + 1;
            while (low < high) {
                long mid = low + (high - low + 1) / 2;
                if (run(prefix, n, l, r, mid).count >= m) low = mid;
                else high = mid - 1;
            }
            State state = run(prefix, n, l, r, low);
            return state.value + low * m;
        }
        final long infinity = 1L << 60;
        long bestSingle = -infinity;
        Deque<Integer> deque = new ArrayDeque<>();
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                while (!deque.isEmpty() && prefix[deque.peekLast()] >= prefix[addIndex]) deque.pollLast();
                deque.addLast(addIndex);
            }
            int minIndex = end - r;
            while (!deque.isEmpty() && deque.peekFirst() < minIndex) deque.pollFirst();
            if (!deque.isEmpty()) {
                long sum = prefix[end] - prefix[deque.peekFirst()];
                if (sum > bestSingle) bestSingle = sum;
            }
        }
        return bestSingle;
    }

    private State run(long[] prefix, int n, int l, int r, long penalty) {
        State[] dp = new State[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = new State();
        Deque<Integer> deque = new ArrayDeque<>();
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                while (!deque.isEmpty() && candidateBetter(dp, prefix, addIndex, deque.peekLast())) deque.pollLast();
                deque.addLast(addIndex);
            }
            int minIndex = end - r;
            while (!deque.isEmpty() && deque.peekFirst() < minIndex) deque.pollFirst();
            dp[end] = new State(dp[end - 1].value, dp[end - 1].count);
            if (!deque.isEmpty()) {
                int start = deque.peekFirst();
                State take = new State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1);
                if (better(take, dp[end])) dp[end] = take;
            }
        }
        return dp[n];
    }

    private boolean candidateBetter(State[] dp, long[] prefix, int a, int b) {
        State left = new State(dp[a].value - prefix[a], dp[a].count);
        State right = new State(dp[b].value - prefix[b], dp[b].count);
        return better(left, right);
    }
}
