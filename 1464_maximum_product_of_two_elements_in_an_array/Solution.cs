// LeetCode 1464 - Maximum Product Of Two Elements In An Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

using System;
public class Solution {
    public int MaxProduct(int[] nums) {
        Array.Sort(nums);
        return (nums[nums.Length - 2] - 1) * (nums[nums.Length - 1] - 1);
    }
}
