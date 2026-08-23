// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

import java.util.PriorityQueue;

class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        PriorityQueue<int[]> h = new PriorityQueue<>((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        for (int i = 0; i < nums.length; i++) {
            h.offer(new int[] {nums[i], i});
        }
        for (int t = 0; t < k; t++) {
            int[] cur = h.poll();
            int v = cur[0] * multiplier;
            int i = cur[1];
            nums[i] = v;
            h.offer(new int[] {v, i});
        }
        return nums;
    }
}
