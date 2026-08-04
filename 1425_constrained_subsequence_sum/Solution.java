// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

import java.util.*;

class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] best = nums.clone();
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!queue.isEmpty() && queue.peekFirst() < i - k) queue.pollFirst();
            best[i] = nums[i] + Math.max(0, queue.isEmpty() ? 0 : best[queue.peekFirst()]);
            while (!queue.isEmpty() && best[queue.peekLast()] <= best[i]) queue.pollLast();
            queue.offerLast(i);
        }
        int ans = best[0];
        for (int v : best) ans = Math.max(ans, v);
        return ans;
    }
}
