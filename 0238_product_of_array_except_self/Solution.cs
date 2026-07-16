// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int length = nums.Length;
        int[] result = new int[length];
        int prefix = 1;
        for (int index = 0; index < length; index++) {
            result[index] = prefix;
            prefix *= nums[index];
        }
        int suffix = 1;
        for (int index = length - 1; index >= 0; index--) {
            result[index] *= suffix;
            suffix *= nums[index];
        }
        return result;
    }
}
