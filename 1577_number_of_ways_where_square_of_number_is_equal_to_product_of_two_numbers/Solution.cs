// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

using System.Collections.Generic;

public class Solution {
    public int NumTriplets(int[] nums1, int[] nums2) {
        return Count(nums1, nums2) + Count(nums2, nums1);
    }

    private int Count(int[] a, int[] b) {
        var squares = new Dictionary<long, int>();
        foreach (int x in a) {
            long sq = (long)x * x;
            squares.TryGetValue(sq, out int c);
            squares[sq] = c + 1;
        }
        var products = new Dictionary<long, int>();
        for (int i = 0; i < b.Length; i++) {
            for (int j = i + 1; j < b.Length; j++) {
                long p = (long)b[i] * b[j];
                products.TryGetValue(p, out int c);
                products[p] = c + 1;
            }
        }
        int ans = 0;
        foreach (var kv in squares) {
            if (products.TryGetValue(kv.Key, out int pc)) ans += kv.Value * pc;
        }
        return ans;
    }
}
