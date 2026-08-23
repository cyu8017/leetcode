// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum_total_sum_with_threshold_constraints/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long maxSum(int[] nums, int[] threshold) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(threshold[a], threshold[b]));
        PriorityQueue<Integer> tree = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        long ans = 0;
        int i = 0;
        for (int step = 1; ; step++) {
            while (i < n && threshold[idx[i]] <= step) {
                tree.offer(nums[idx[i]]);
                i++;
            }
            if (tree.isEmpty()) break;
            ans += tree.poll();
        }
        return ans;
    }
}
