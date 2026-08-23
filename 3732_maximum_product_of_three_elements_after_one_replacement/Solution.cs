// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

using System;

public class Solution {
    public long MaxProduct(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        long a = nums[0], b = nums[1], c = nums[n - 2], d = nums[n - 1];
        const long x = 100000;
        return Math.Max(Math.Max(a * b * x, c * d * x), -a * d * x);
    }
}
