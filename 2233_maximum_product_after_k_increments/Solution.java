// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

import java.util.PriorityQueue;

class Solution {
    public int maximumProduct(int[] nums, int k) {
        final int MOD = 1_000_000_007;
        PriorityQueue<Integer> h = new PriorityQueue<>();
        for (int x : nums) h.offer(x);
        for (int i = 0; i < k; i++) {
            int x = h.poll();
            h.offer(x + 1);
        }
        long ans = 1;
        while (!h.isEmpty()) {
            ans = ans * h.poll() % MOD;
        }
        return (int) ans;
    }
}
