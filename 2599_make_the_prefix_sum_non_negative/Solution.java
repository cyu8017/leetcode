// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

import java.util.PriorityQueue;

class Solution {
    public int makePrefSumNonNegative(int[] nums) {
        PriorityQueue<Integer> h = new PriorityQueue<>();
        long sum = 0;
        int ans = 0;
        for (int x : nums) {
            sum += x;
            if (x < 0) h.offer(x);
            if (sum < 0) {
                int worst = h.poll();
                sum -= worst;
                ans++;
            }
        }
        return ans;
    }
}
