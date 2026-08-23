// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long maxSum(int[][] grid, int[] limits, int k) {
        PriorityQueue<Integer> h = new PriorityQueue<>();
        long sum = 0;
        for (int i = 0; i < grid.length; i++) {
            int[] r = grid[i].clone();
            Arrays.sort(r);
            int lim = limits[i];
            if (lim > r.length) lim = r.length;
            for (int j = 0; j < lim; j++) {
                int val = r[r.length - 1 - j];
                h.offer(val);
                sum += val;
                if (h.size() > k) sum -= h.poll();
            }
        }
        return sum;
    }
}
