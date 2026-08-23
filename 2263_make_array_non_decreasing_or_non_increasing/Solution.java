// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

import java.util.PriorityQueue;

class Solution {
    private int cost(int[] arr) {
        PriorityQueue<Integer> h = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        int ans = 0;
        for (int x : arr) {
            if (!h.isEmpty() && h.peek() > x) {
                int t = h.poll();
                ans += t - x;
                h.offer(x);
            }
            h.offer(x);
        }
        return ans;
    }

    public int convertArray(int[] nums) {
        int[] rev = new int[nums.length];
        for (int i = 0; i < nums.length; i++) rev[i] = nums[nums.length - 1 - i];
        return Math.min(cost(nums), cost(rev));
    }
}
