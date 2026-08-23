// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

using System.Collections.Generic;

public class Solution {
    public int MaximumProduct(int[] nums, int k) {
        const int MOD = 1000000007;
        var h = new PriorityQueue<int, int>();
        foreach (int x in nums) h.Enqueue(x, x);
        for (int i = 0; i < k; i++) {
            h.TryDequeue(out int x, out _);
            h.Enqueue(x + 1, x + 1);
        }
        long ans = 1;
        while (h.Count > 0) {
            h.TryDequeue(out int x, out _);
            ans = ans * x % MOD;
        }
        return (int)ans;
    }
}
