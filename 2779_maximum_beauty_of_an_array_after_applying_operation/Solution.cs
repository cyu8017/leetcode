// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

using System;

public class Solution {
    public int MaximumBeauty(int[] nums, int k) {
        Array.Sort(nums);
        int ans = 0, left = 0;
        for (int right = 0; right < nums.Length; right++) {
            while (nums[right] - nums[left] > 2 * k) left++;
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
