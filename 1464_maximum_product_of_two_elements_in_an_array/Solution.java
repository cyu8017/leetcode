// LeetCode 1464 - Maximum Product Of Two Elements In An Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

import java.util.*;

class Solution {
    public int maxProduct(int[] nums) {
        Arrays.sort(nums);
        return (nums[nums.length - 2] - 1) * (nums[nums.length - 1] - 1);
    }
}
