// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

public class Solution {
    public int MaxProductDifference(int[] nums) {
        int a = 0, b = 0, c = 100000, d = 100000;
        foreach (int x in nums) {
            if (x > a) { b = a; a = x; }
            else if (x > b) b = x;
            if (x < c) { d = c; c = x; }
            else if (x < d) d = x;
        }
        return a * b - c * d;
    }
}